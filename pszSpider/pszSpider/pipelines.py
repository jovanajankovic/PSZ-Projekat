# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
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
            stanje VARCHAR(16),
            marka VARCHAR(32),
            model VARCHAR(32),
            godiste VARCHAR(5),
            kilometraza VARCHAR(16),
            karoserija VARCHAR(32),
            gorivo VARCHAR(32),
            kubikaza VARCHAR(16),
            motor VARCHAR(32),
            menjac VARCHAR(64),
            broj_vrata VARCHAR(16),
            broj_sedista VARCHAR(16),
            klima VARCHAR(16),
            boja VARCHAR(16),
            ostecenje VARCHAR(32),
            lokacija VARCHAR(32),
            cena VARCHAR(32),
            PRIMARY KEY (id)
        )
        """)
    
    def process_item(self, item, spider):
        self.cur.execute(""" insert into cars (stanje, marka, model, godiste, kilometraza, karoserija, gorivo, kubikaza, motor, menjac, broj_vrata, broj_sedista, klima, boja, ostecenje, lokacija, cena) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
            item["stanje"],
            item["marka"],
            item["model"],
            item["godiste"],
            item["kilometraza"],
            item["karoserija"],
            item["gorivo"],
            item["kubikaza"],
            item["motor"],
            item["menjac"],
            item["broj_vrata"],
            item["broj_sedista"],
            item["klima"],
            item["boja"],
            item["ostecenje"],
            item["lokacija"],
            item["cena"],
        ))
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()