from scrapy import Spider, Request
from scrapy.linkextractors import LinkExtractor
from qiubai3.items import Qiubai3Item

class QiubaiSpider(Spider):
    name = 'QSBK'
    start_urls = [
        'http://www.qiushibaike.com/',
    ]

    def parse(self,response):
        extractor = LinkExtractor(allow='/article/*')
        links = extractor.extract_links(response)
        for link in links:
            req = Request(link.url, self.parse_detail_page)
            item = Qiubai3Item()
            req.meta['item'] = item
            yield req

    def parse_detail_page(self,response):
        item = response.meta["item"]
        item['author'] = response.xpath('//div[@class="author clearfix"/a[2]/h2/text()').extract()[0]
        item['content'] = response.xpath('//div[@class="content"/text()').extract()[0]
        item['comment_name'] = response.xpath('//div[@class="cmt-name"/text()').extract()[0]
        item['comment'] = response.xpath('//div[@class="main-text"/text()').extract()[0]
        yield item