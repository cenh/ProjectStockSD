import scrapy, base64, urllib2, re, os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging


# this does not work, why? I don't like scrapy's insane debug output
configure_logging({'LOG_ENABLED': False, 'LOG_LEVEL': 'WARNING'}, install_root_handler=False)


def extract_from_xpath(response, x_path):
    info = response.xpath(x_path).extract_first()
    if info is None:
        return ''
    else:
        return info

def extract_from_regex(regex, raw_string):
    match = re.match(regex, raw_string)
    if match is None:
        return ''
    else:
        return match.group(1)




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
    name = 'diku' #Required by Scrapy attribute.
    #allowed_domains = ['diku.dk']
    #url = 'http://www.diku.dk/Ansatte'
    test_file_path = os.path.dirname(os.path.abspath(__file__)) + '/supervisordetail-test.html'
    url_local = 'file://127.0.0.1' + test_file_path
    url = url_local
    start_urls = [url]
    items = []



    def parse(self, response):
        if self.url == 'http://www.diku.dk/Ansatte':
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
        else:
            item = DikuAnsatteItem()
            item['profile_link'] = 'pure' #Really bad for unit testing.
            request = scrapy.Request(self.url_local, callback=self.parse_detail)
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

        item['name'] = extract_from_xpath(response, name_tag)

        item['status'] = extract_from_xpath(response, title_tag)

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

        item['phone'] = extract_from_xpath(response, '//span[@class="property person_contact_phone"]/text()')

        item['phone_internal'] = '' # doesn't seem to exist for pure links

        item['fax'] = extract_from_xpath(response, '//span[@class="property person_contact_fax"]/text()')

        item['mobile'] = extract_from_xpath(response, '//span[@class="property person_contact_mobilephone"]/text()')

        item['workplace'] = extract_from_xpath(response, '//div[@class="address"]/p/text()')

        item['email'] = extract_from_xpath(response, '//ul[@class="relations email"]/li/a/span/text()')

        item['location'] = '' # this also doesn't seem to exist

        self.items.append(item)
        yield item

    def parse_other(self, response):
        item = response.meta['item']

        email = response.xpath('//p[@class="forskerprofil_kontakt"]/a/text()').extract()
        item['email'] = ''.join(email) if len(email) > 0 else ''

        #List can contain more than one element.
        workplace = response.xpath('//p[@class="forskerprofil_adresse"]/text()').extract()
        if workplace:
            item['workplace'] = ', '.join(workplace)

        #List can contain more than one element.
        contact_info = response.xpath('//p[@class="forskerprofil_kontakt"]/text()').extract()
        for c in contact_info:

            item['location'] = extract_from_regex('Kontor:\s+(.*)', c)

            item['phone'] = extract_from_regex('Telefon:\s+(.*)', c)

            item['phone_internal'] = extract_from_regex('Telefon (Sekretariat):\s(.*)', c)

            item['fax'] = extract_from_regex('Fax:\s+(.*)', c)

            item['mobile'] = extract_from_regex('Mobil:\s+(.*)', c)

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
    print "\n \n \n len(spider) is \n \n \n"
    print len(spider.items)
