# -*- coding: utf-8 -*-
import scrapy
import json


class Weibo2Spider(scrapy.Spider):
    name = "weibo2"
    start_urls = ['https://passport.weibo.cn/signin/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': '471530660@qq.com', 'password': 'ji88883993'},
            callback=self.after_login,
            method='POST',
            url='https://passport.weibo.cn/sso/login'
        )

    def after_login(self, response):
        for i in range(5):
            yield scrapy.Request(
                'http://m.weibo.cn/index/feed?format=cards&next_cursor=4038154267119887&page=%s' % (i+1), self.home)

    def home(self, response):
        objs = json.loads(response.body)
        obj = objs[0]
        for item in obj['card_group']:
            print item['mblog']['text']


