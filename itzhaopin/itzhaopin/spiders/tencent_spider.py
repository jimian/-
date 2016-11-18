# -*- coding: utf-8 -*-
import scrapy


class TencentSpiderSpider(scrapy.Spider):
    name = "tencent_spider"
    allowed_domains = ["http://hr.tencent.com/position.php"]
    start_urls = (
        'http://www.http://hr.tencent.com/position.php/',
    )

    def parse(self, response):
        pass
