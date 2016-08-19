# -*- coding: utf-8 -*-
import scrapy
from tianya.items import TianyaItem

class TianyaSpider(scrapy.Spider):
    name = "tianya"
    allowed_domains = ["http://bbs.tianya.cn/"]
    start_urls = [
        "http://bbs.tianya.cn/list.jsp?item=funinfo&grade=3&order=1"
    ]

    # for sel in response.xpath('//ul/li'):
    #     item = DmozItem()
    #     item['title'] = sel.xpath('a/text()').extract()
    #     item['link'] = sel.xpath('a/@href').extract()
    #     item['desc'] = sel.xpath('text()').extract()
    #     yield item

    def parse(self, response):
        for sel in response.xpath('//tbody/tr/td/a'):
            item = TianyaItem()
            item['title'] = sel.xpath('text()').extract()
            item['link'] = sel.xpath('@href').extract()
            yield item