import scrapy, os
from scrapy.crawler import CrawlerProcess


def extract_info(response, x_path):
    info = response.xpath(x_path).extract()
    if len(info) > 0:
        return info
    else:
        return ''

class TestSpiderItems(scrapy.Item):
    name = scrapy.Field()


class TestSpider(scrapy.Spider):
    test_file_path = os.path.dirname(os.path.abspath(__file__)) + '/supervisordetail-test.html'
    url = 'file://127.0.0.1' + test_file_path
    name = 'Test Spider'
    items = []

    def start_requests(self):
        yield scrapy.Request(self.url, self.parse_detail)

    def parse_detail(self, response):
        #item = response.meta['item']
        item = TestSpiderItems()
        x_tag_person = '//span[@class="person"]/text()'
        item['name'] = extract_info(response, x_tag_person)
        self.items.append(item)



spider_instance = TestSpider()

process = CrawlerProcess()
process.crawl(spider_instance)
process.start()
print spider_instance.items
