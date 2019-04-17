# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from urllib.parse import quote
from lxml import etree


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['http://search.dangdang.com/']
    # start_urls = ['http://http://search.dangdang.com/']
    base_url = 'http://search.dangdang.com/?key='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORD'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.base_url + quote(keyword)
                yield scrapy.Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        html = response.text
        tree = etree.HTML(html)
        li_list = tree.xpath('//*[@id="component_59"]/li')
        for li in li_list:
            item = DangdangItem()
            item['title'] = li.xpath('./a/@title')
            item['miaoshu'] = li.xpath('./p[@class = "detail"]/text()')   # 之前的爬虫写错了导致抓到的title和miaoshu放在一个了
            # print(li)
            print(item['title'])
            yield item
