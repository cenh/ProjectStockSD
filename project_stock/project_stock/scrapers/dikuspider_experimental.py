import scrapy, base64, urllib2, re, os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging


# this does not work, why? I don't like scrapy's insane debug output
configure_logging({'LOG_ENABLED': False, 'LOG_LEVEL': 'WARNING'}, install_root_handler=False)

class SpiderTestItems(scrapy.Item):
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


#Function for passing information.
def parse_info(item_name, x_path, item):
    info_to_extract = response.xpath(x_path).extract()
    if len(info_to_extract) > 0:
        item[item_name] = info_to_extract
    else:
        item[item_name] = ''

class SpiderTest(scrapy.Spider):
    test_file_path = os.path.dirname(os.path.abspath(__file__)) + "/supervisordetail-test.html"
    name = 'spider_test' #Required by Scrapy attribute.
    start_urls = ["file://127.0.0.1" + test_file_path]
    #allowed_domains = ["file://127.0.0.1"] #Optional attribute.

    def parse(self, reposense):



'''
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


    def parse1(self, response):
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

        name = response.xpath(name_tag).extract()
        item['name'] = name[0] if name else ''

        title = response.xpath(title_tag).extract()
        item['status'] = title[0] if title else ''

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

        phone = response.xpath('//span[@class="property person_contact_phone"]/text()').extract()
        item['phone'] = phone[0] if len(phone) > 0 else ''

        item['phone_internal'] = '' # doesn't seem to exist for pure links

        fax = response.xpath('//span[@class="property person_contact_fax"]/text()').extract()
        item['fax'] = fax[0] if len(fax) > 0 else ''

        mobile = response.xpath('//span[@class="property person_contact_mobilephone"]/text()').extract()
        item['mobile'] = mobile[0] if len(mobile) > 0 else ''

        workplace = response.xpath('//div[@class="address"]/p/text()').extract()
        item['workplace'] = workplace[0] if len(workplace) > 0 else ''

        email = response.xpath('//ul[@class="relations email"]/li/a/span/text()').extract()
        item['email'] = email[0] if len(email) > 0 else ''

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
    #test_file_path = os.path.dirname(os.path.abspath(__file__)) + "/supervisordetail-test.html"
    #spider.start_urls = ["file://127.0.0.1" + test_file_path]
    #spider.allowed_domains = ["file://127.0.0.1"]
    print "\n \n Starting scraping \n \n"
    #print spider.start_urls[0]
    spider.start()
    items_test = len(spider.items)
    print "\n \n \n Printing items_test... \n \n \n"
    print items_test
'''
