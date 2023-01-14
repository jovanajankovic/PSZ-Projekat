import scrapy
import random 

class CarsSpider(scrapy.Spider):
    name = "cars"

    start_urls = [
         "https://www.polovniautomobili.com/auto-oglasi/pretraga?brand=&price_to=&year_from=&year_to=&showOldNew=all&submit_1=&without_price=1"
    ]

    def parse(self, response):
        car_page_links = response.css('a.ga-title')
        yield from response.follow_all(car_page_links, callback = self.parse_car)

        next_page = response.css('a.js-pagination-next:last-of-type')
        yield from response.follow_all(next_page, callback = self.parse)

    def parse_car(self, response):

        def extract_with_css(query):
            return response.css(query).get(default = '').strip()

        yield {
            'stanje': extract_with_css('div.uk-width-1-2:contains("Stanje") + div.uk-text-bold::text'),
            'marka': extract_with_css('div.uk-width-1-2:contains("Marka") + div.uk-text-bold::text'),
            'model': extract_with_css('div.uk-width-1-2:contains("Model") + div.uk-text-bold::text'),
        }