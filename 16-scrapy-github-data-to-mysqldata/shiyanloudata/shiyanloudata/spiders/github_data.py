# -*- coding: utf-8 -*-
import scrapy
from shiyanloudata.items import ShiyanloudataItem

class GithubDataSpider(scrapy.Spider):
    name = 'github_data'

    @property
    def start_urls(self):
        url_tmpl = [
                'https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories']
        return url_tmpl

    def parse(self, response):
        for data in response.xpath('//li[contains(@class, "col-12")]'):
            item = ShiyanloudataItem({
                'name':data.xpath('.//a/text()').extract_first().strip(),
                'update_time':data.xpath('.//relative-time/@datetime').extract_first()
                })
            yield item
