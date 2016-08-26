# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

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
        for sel in response.xpath('//tbody/tr'):
            item = TianyaItem()
            item['title'] = sel.xpath('normalize-space(td[1]/a/text())').extract()
            item['link'] = sel.xpath('td[1]/a/@href').extract()
            item['author'] = sel.xpath('td[2]/a/text()').extract()
            item['click'] = sel.xpath('td[3]/text()').extract()
            item['reply'] = sel.xpath('td[4]/text()').extract()
            yield item