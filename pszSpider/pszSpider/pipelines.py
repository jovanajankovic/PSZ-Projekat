# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class PszspiderPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'psz-projekat'
        )
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS cars(
            id int NOT NULL auto_increment, 
            stanje VARCHAR(255),
            marka VARCHAR(255),
            model VARCHAR(255),
            PRIMARY KEY (id)
        )
        """)
    
    def process_item(self, item, spider):
        self.cur.execute(""" insert into cars (stanje, marka, model) values (%s,%s,%s)""", (
            item["stanje"],
            item["marka"],
            item["model"]
        ))
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()