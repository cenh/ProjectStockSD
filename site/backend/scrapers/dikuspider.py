import scrapy, base64, urllib2
from scrapy.crawler import CrawlerProcess

class DikuAnsatteItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    profile_link = scrapy.Field()
    photo = scrapy.Field()
    tel = scrapy.Field()
    email = scrapy.Field()


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

                # maybe add email from here since it's difficult to get from detail page
                #item['email'] = ...
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

        name = response.xpath(name_tag).extract()
        item['name'] = name[0] if name else None

        title = response.xpath(title_tag).extract()
        item['title'] = title[0] if title else None

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
