import scrapy, base64, urllib2, re
from scrapy.crawler import CrawlerProcess

class DikuAnsatteItem(scrapy.Item):
    name = scrapy.Field() # check
    title = scrapy.Field() # check
    profile_link = scrapy.Field() # check
    photo = scrapy.Field() # check
    email = scrapy.Field() # check
    tel = scrapy.Field() # check
    tel_internal = scrapy.Field()
    fax = scrapy.Field()
    cell = scrapy.Field()
    workplace = scrapy.Field() # check
    location = scrapy.Field()


class DikuAnsatteSpider(scrapy.Spider):
    name = 'diku'
    allowed_domains = ['diku.dk']
    start_urls = [
        'http://www.diku.dk/Ansatte',
    ]
    items = []

    def parse(self, response):
        for sel in response.xpath('//table[@id="medarbejdertable"]/tbody/tr'):
            for a in sel.xpath('td/a'):
                name = a.xpath('text()').extract()
                if not name or name[0] == 'E-mail':
                    break

                item = DikuAnsatteItem()

                item['profile_link'] = response.urljoin(a.xpath('@href').extract()[0])
                request = scrapy.Request(item['profile_link'], callback=self.parse_detail)
                request.meta['item'] = item
                yield request

    def parse_detail(self, response):
        item = response.meta['item']

        # distinguish between the two link types, they have different formats
        if 'pure' in item['profile_link']:
            name_tag = '//span[@class="person"]/text()'
            title_tag = '//p[@class="type"]/text()'
            photo_tag = '//div[@class="person_photo"]/img/@src'

            workplace = response.xpath('//div[@class="address"]/p/text()').extract()
            item['workplace'] = workplace[0] if len(workplace) > 0 else ''

            email = response.xpath('//ul[@class="relations email"]/li/a/span/text()').extract()
            item['email'] = email[0] if len(email) > 0 else ''
        else:
            name_tag = '//div[@id="forskerprofil_kontaktoplysninger"]/h1/text()'
            title_tag = '//p[@class="forskerprofil_titel"]/text()'
            photo_tag = '//div[@id="forskerprofil_kontaktoplysninger"]/img/@src'

            email = response.xpath('//p[@class="forskerprofil_kontakt"]/a/text()').extract()
            item['email'] = ''.join(email) if len(email) > 0 else ''

            workplace = response.xpath('//p[@class="forskerprofil_adresse"]/text()').extract()
            if workplace:
                item['workplace'] = ', '.join(workplace)

            contact_info = response.xpath('//p[@class="forskerprofil_kontakt"]/text()').extract()
            for c in contact_info:
                location = re.match('Kontor:\s+(.*)', c)
                if location:
                    item['location'] = location.group(1)

                tel = re.match('Telefon:\s+(.*)', c)
                if tel:
                    item['tel'] = tel.group(1)

                tel_internal = re.match('Telefon (Sekretariat):\s(.*)', c)
                if tel_internal:
                    item['tel_internal'] = tel_internal.group(1)

                fax = re.match('Fax:\s+(.*)', c)
                if fax:
                    item['fax'] = fax.group(1)

                cell = re.match('Mobil:\s+(.*)', c)
                if cell:
                    item['cell'] = cell.group(1)

        name = response.xpath(name_tag).extract()
        item['name'] = name[0] if name else ''

        title = response.xpath(title_tag).extract()
        item['title'] = title[0] if title else ''

        photo_url = response.xpath(photo_tag).extract()
        if photo_url:
            photo = urllib2.urlopen(photo_url[0]).read()
            item['photo'] = base64.b64encode(photo) # save photo as base64
        else:
            item['photo'] = ''

        # the rest will need regexes I believe

        self.items.append(item)

        yield item

    def start(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(self)
        process.start()


# testing
if __name__ == '__main__':
    DikuAnsatteSpider().start()
