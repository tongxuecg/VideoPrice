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
    region_code = scrapy.Field()
    asin = scrapy.Field()
    

    
