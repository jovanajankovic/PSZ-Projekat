import scrapy
from scrapy.exceptions import CloseSpider

MAX_CAR_NUM = 20000

class CarsSpider(scrapy.Spider):
    name = "cars"

    start_urls = [
         "https://www.polovniautomobili.com/auto-oglasi/pretraga?brand=&price_to=&year_from=&year_to=&showOldNew=all&submit_1=&without_price=1"
    ]

    parsed_cars = 0

    def parse(self, response):
        try:   
            car_page_links = response.css('a.ga-title')
            yield from response.follow_all(car_page_links, callback = self.parse_car)
            next_page = response.css('a.js-pagination-next:last-of-type')
            yield from response.follow_all(next_page, callback = self.parse)
        except Exception:
            print('exception occured')
    
      
    def parse_car(self, response):
        if self.parsed_cars < MAX_CAR_NUM:
            self.parsed_cars = self.parsed_cars + 1
            def extract_with_css(query):
                return response.css(query).get(default = '').strip()

            yield {
                'stanje': extract_with_css('div.uk-width-1-2:contains("Stanje") + div.uk-text-bold::text'),
                'marka': extract_with_css('div.uk-width-1-2:contains("Marka") + div.uk-text-bold::text'),
                'model': extract_with_css('div.uk-width-1-2:contains("Model") + div.uk-text-bold::text'),
                'godiste': extract_with_css('div.uk-width-1-2:contains("Godište") + div.uk-text-bold::text'),
                'kilometraza': extract_with_css('div.uk-width-1-2:contains("Kilometraža") + div.uk-text-bold::text'),
                'karoserija': extract_with_css('div.uk-width-1-2:contains("Karoserija") + div.uk-text-bold::text'),
                'gorivo': extract_with_css('div.uk-width-1-2:contains("Gorivo") + div.uk-text-bold::text'),
                'kubikaza': extract_with_css('div.uk-width-1-2:contains("Kubikaža") + div.uk-text-bold::text'),
                'motor': extract_with_css('div.uk-width-1-2:contains("Snaga motora") + div.uk-text-bold::text'),
                'menjac': extract_with_css('div.uk-width-1-2:contains("Menjač") + div.uk-text-bold::text'),
                'broj_vrata': extract_with_css('div.uk-width-1-2:contains("Broj vrata") + div.uk-text-bold::text'),
                'broj_sedista': extract_with_css('div.uk-width-1-2:contains("Broj sedišta") + div.uk-text-bold::text'),
                'klima': extract_with_css('div.uk-width-1-2:contains("Klima") + div.uk-text-bold::text'),
                'boja': extract_with_css('div.uk-width-1-2:contains("Boja") + div.uk-text-bold::text'),
                'ostecenje': extract_with_css('div.uk-width-1-2:contains("Oštećenje") + div.uk-text-bold::text'),
                'lokacija': extract_with_css('div.infoBox.js-tutorial-contact div.uk-grid.uk-margin-top-remove div.uk-width-1-2::text'),
                'cena': extract_with_css('span.priceClassified.regularPriceColor::text')
            }
        else:
            raise CloseSpider("all data was successfully retrieved")
            