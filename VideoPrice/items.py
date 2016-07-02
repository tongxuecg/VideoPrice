import scrapy


class VideobaseItem(scrapy.Item):
    # base infos table
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

    # Aama_his_datas table
    Abottom_price = scrapy.Field()
    Abottom_time = scrapy.Field()

    # Bama_his_datas table
    Bbottom_price = scrapy.Field()
    Bbottom_time = scrapy.Field()

    #Aama_real_time_price table
    Areal_time_price = scrapy.Field()

    #Bama_real_time_price table
    Breal_time_price = scrapy.Field()

    

    

    

    
