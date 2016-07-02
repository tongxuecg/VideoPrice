# -*- coding: utf-8 -*-


import MySQLdb
import datetime


class MySQLStorePipeline(object):
  def __init__(self):
    self.conn = MySQLdb.connect(user='root', passwd='123456', db='VideoPrice', host='localhost', unix_socket='/dev/shm/mysqld.sock', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()
    #清空表：
    self.cursor.execute("delete from baseinfo;")
    self.conn.commit() 
  def process_item(self, item, spider): 
    curTime =  datetime.datetime.now()  
    try:
      self.cursor.execute("""INSERT INTO baseinfo (asin, country, company, year, film_time, time_to_market, video_coding,resolution,dialogue,subtitle,region_code,Abottom_price,Abottom_time,Areal_time_price,Bbottom_price,Bbottom_time,Breal_time_price)  
              VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s)""", 
              (
              	item['asin'][0].encode('utf-8'),
                item['country'][0].encode('utf-8'), 
                item['company'][0].encode('utf-8'),
                item['year'][0].encode('utf-8'),
                item['film_time'][0].encode('utf-8'),
                item['time_to_market'][0].encode('utf-8'),
                item['video_coding'][0].encode('utf-8'),
                item['resolution'][0].encode('utf-8'),
                item['dialogue'][0].encode('utf-8'),
                item['subtitle'][0].encode('utf-8'),
                item['region_code'][0].encode('utf-8'),
                item['Abottom_price'][0].encode('utf-8'),
                item['Abottom_time'][0].encode('utf-8'),
                item['Areal_time_price'][0].encode('utf-8'),
                item['Bbottom_price'][0].encode('utf-8'),
                item['Bbottom_time'][0].encode('utf-8'),
                #item['Breal_time_price'][0].encode('utf-8'),

                curTime,
              )
      )
      self.conn.commit()
    except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
    return item