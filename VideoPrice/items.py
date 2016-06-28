import scrapy


class VideobaseItem(scrapy.Item):
    
    country = scrapy.Field()
    company = scrapy.Field()
    year = scrapy.Field()
    film_time = scrapy.Field()
    time_to_market = scrapy.Field()
    video_coding = scrapy.Field()
    resolution = scrapy.Field()
    dialogue = scrapy.Field()
    subtitle = scrapy.Field()
    region_code = scrapy.Field()
    asin = scrapy.Field()

class Aama_his_datas(scrapy.Item):
	Abottom_price = scrapy.Field()
	Abottom_time = scrapy.Field()

class Bama_his_datas(scrapy.Item):
	Bbottom_price = scrapy.Field()
	Bbottom_time = scrapy.Field()

class Aama_real_time_price(scrapy.Item):
	Areal_time_price = scrapy.Field()

class Bama_real_time_price(scrapy.Item):
	Breal_time_price = scrapy.Field()

	

	

    

    
