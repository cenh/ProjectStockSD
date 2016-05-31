import scrapy, base64, urllib2, re, os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging


# this does not work, why? I don't like scrapy's insane debug output
configure_logging({'LOG_ENABLED': False, 'LOG_LEVEL': 'WARNING'}, install_root_handler=False)


def extract_info(response, x_path):
    info = response.xpath(x_path).extract_first()
    if info is None:
        return ''
    else:
        return info

class DikuAnsatteItem(scrapy.Item):
    name = scrapy.Field()
    status = scrapy.Field() # this should be renamed, both here and in models, to title
    profile_link = scrapy.Field()
    photo = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    phone_internal = scrapy.Field()
    fax = scrapy.Field()
    mobile = scrapy.Field()

    workplace = scrapy.Field() # maybe these two should be merged together?
    location = scrapy.Field()

    # perhaps scrape website as well?

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
        else:
            name_tag = '//div[@id="forskerprofil_kontaktoplysninger"]/h1/text()'
            title_tag = '//p[@class="forskerprofil_titel"]/text()'
            photo_tag = '//div[@id="forskerprofil_kontaktoplysninger"]/img/@src'

        item['name'] = extract_info(response, name_tag)

        item['status'] = extract_info(response, title_tag)

        photo_url = response.xpath(photo_tag).extract()
        if photo_url:
            photo = urllib2.urlopen(photo_url[0]).read()
            item['photo'] = base64.b64encode(photo) # save photo as base64
        else:
            item['photo'] = ''

        # parse things they do not have in common, separately
        if 'pure' in item['profile_link']:
            return self.parse_pure(response)
        else:
            return self.parse_other(response)

    def parse_pure(self, response):
        item = response.meta['item']

        item['phone'] = extract_info(response, '//span[@class="property person_contact_phone"]/text()')

        item['phone_internal'] = '' # doesn't seem to exist for pure links

        item['fax'] = extract_info(response, '//span[@class="property person_contact_fax"]/text()')

        item['mobile'] = extract_info(response, '//span[@class="property person_contact_mobilephone"]/text()')

        item['workplace'] = extract_info(response, '//div[@class="address"]/p/text()')

        item['email'] = extract_info(response, '//ul[@class="relations email"]/li/a/span/text()')

        item['location'] = '' # this also doesn't seem to exist

        self.items.append(item)
        yield item

    def parse_other(self, response):
        item = response.meta['item']

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

            phone = re.match('Telefon:\s+(.*)', c)
            if phone:
                item['phone'] = phone.group(1)

            phone_internal = re.match('Telefon (Sekretariat):\s(.*)', c)
            if phone_internal:
                item['phone_internal'] = phone_internal.group(1)

            fax = re.match('Fax:\s+(.*)', c)
            if fax:
                item['fax'] = fax.group(1)

            mobile = re.match('Mobil:\s+(.*)', c)
            if mobile:
                item['mobile'] = mobile.group(1)

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
    spider = DikuAnsatteSpider()
    spider.start()
