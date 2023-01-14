# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PszspiderItem(Item):
    stanje = Field()
    marka = Field()
    model = Field()
