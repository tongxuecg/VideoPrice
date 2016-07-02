# -*- coding: utf-8 -*

import scrapy
import urllib,re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from VideoPrice.items import VideobaseItem
import request

class DpwSpider(CrawlSpider):
    name = "baseinfo"
    allowed_domains = ["blu-ray.com","amazon.com","camelcamelcamel.com"]
    #start_urls = ["http://www.blu-ray.com/movies/"]
    start_urls = ["http://www.blu-ray.com/movies/The-X-Files-Event-Series-Blu-ray/147436/"]

    
    #rules = [ Rule(SgmlLinkExtractor(allow=['/*/[0-9]{1,6}/']), callback='web_parse', follow=True) ]

    def parse(self, response):
        sel = Selector(response)
        item = VideobaseItem() 

        country=sel.xpath('//table[@width="1262"]//td[@width="518"]/img/@title').extract()
        item['country']=country

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

        item['asin']=tmp=re.findall(r'(?<=dp\/).+?(?=\?)',new_link)    
        Asearch_link = "%s%s" % ('http://camelcamelcamel.com/search?sq=',''.join(tmp))
        Bsearch_link = "%s%s" % ('http://uk.camelcamelcamel.com/search?sq=',''.join(tmp))
        A_real_price = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%%3Daps&field-keywords=%s&rh=i%%3Aaps%%2Ck%%3AB00YHRMI3O" %  ''.join(tmp)
        B_real_price = "https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%%3Daps&field-keywords=%s&rh=i%%3Aaps%%2Ck%%3AB00YHRMI3O"  %  ''.join(tmp)

        

        yield scrapy.Request(url=Asearch_link,meta={'item':item},callback=self.A_pase,dont_filter=True)

        yield scrapy.Request(url=Bsearch_link,meta={'item':item},callback=self.B_pase,dont_filter=True)

        yield scrapy.Request(url=A_real_price,meta={'item':item},callback=self.A_real_price,dont_filter=True)
   
        yield scrapy.Request(url=B_real_price,meta={'item':item},callback=self.B_real_price,dont_filter=True)
        

    def A_real_price(self,response):   

        item = response.meta['item']
        sel = Selector(response)
        site=sel.xpath('//ul[@id="s-results-list-atf"]//div[@class="a-row a-spacing-none"]//a[@class="a-link-normal a-text-normal"]')

        
        item['Areal_time_price']=site.xpath('span/text()').extract()
        
        
        

    def B_real_price(self,response):   

        item = response.meta['item']
        sel = Selector(response)
        site=sel.xpath('//div[@id="resultsCol"]//div[@id="a-row a-spacing-none"]')

        
        item['Breal_time_price']=site.xpath('//span/text()').extract()
        
        return item


    def A_pase(self,response):   

        item = response.meta['item']
        sel = Selector(response)
        site=sel.xpath('//div[@id="section_amazon"]//table[@class="product_pane"]//tr[@class="lowest_price"]')

        
        item['Abottom_price']=site.xpath('td[2]/text()').extract()

        item['Abottom_time']=site.xpath('td[3]/text()').extract()




    def B_pase(self,response):   


        item = response.meta['item']
        sel = Selector(response)
        
        site=sel.xpath('//div[@id="section_new"]//table[@class="product_pane"]//tr[@class="lowest_price"]')

        item['Bbottom_price']=site.xpath('td[2]/text()').extract()

        item['Bbottom_time']=site.xpath('td[3]/text()').extract()

        



        

