from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class QiubaiSpider(CrawlSpider):
    name = 'Qiubai'
    start_url = ['http://www.qiushibaike.com/']
    rules = [
        Rule(LinkExtractor(allow='/article/*')),
        Rule(LinkExtractor(allow='/users/*'), callback='parse_result'),
    ]

    def parse_result(self, response):
        print response.xpath('//div[@class=user-header-cover]/h2/text()').extract()[0]
