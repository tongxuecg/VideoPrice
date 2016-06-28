# -*- coding: utf-8 -*

import scrapy
import urllib,re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from VideoPrice.items import VideobaseItem

class DpwSpider(CrawlSpider):
    name = "baseinfo"
    allowed_domains = ["blu-ray.com"]
    #start_urls = ["http://www.blu-ray.com/movies/"]
    start_urls = ["http://www.blu-ray.com/movies/The-X-Files-Event-Series-Blu-ray/147436/"]

    
    #rules = [ Rule(SgmlLinkExtractor(allow=['/*/[0-9]{1,6}/']), callback='web_parse', follow=True) ]

    def parse(self, response):
        sel = Selector(response)
        site = sel.xpath('//div[@itemprop="review"]')

        item = VideobaseItem() 

        country=''
        company=sel.xpath('//span[@class="subheading"]/a[1]/text()').extract()
        item['company']=company  

        year=sel.xpath('//span[@class="subheading"]/a[2]/text()').extract() 
        item['year']=year

        film_time=sel.xpath('//span[@class="subheading"]/span/text()').extract()
        item['film_time']=film_time 

        time_to_market=sel.xpath('//span[@class="subheading"]/a[3]/text()').extract() 
        item['time_to_market']=time_to_market

        desc=sel.xpath('//td[@width="228px"]/text()').extract() 
        scode=''.join(desc[1]).split(':')[1]
        item['video_coding']=''.join(scode).strip()
        
        Resolution=''.join(desc[2]).split(':')[1]
        item['resolution']=''.join(Resolution).strip()

        Region=''.join(desc[-1]).strip()
        item['region_code']=Region

        #以下两个字段需要进一步处理
        dialogue=sel.xpath('//td[@width="228px"]/div[@id="shortaudio"]/div/text()').extract() 
        item['dialogue']=dialogue

        subtitle=sel.xpath('//td[@width="228px"]/div[@id="shortsubs"]/text()').extract() 
        item['subtitle']=subtitle

        #ASIN码的处理
        asin=sel.xpath('//a[@id="movie_buylink"]/@href').extract()      
        link_tmp=''.join(asin)
        new_link=urllib.urlopen(link_tmp).geturl()

        item['asin']=re.findall(r'(?<=dp\/).+?(?=\?)',new_link)

        return item


        

