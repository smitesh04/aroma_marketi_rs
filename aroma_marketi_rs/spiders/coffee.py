import os

import scrapy
from scrapy.cmdline import execute
from aroma_marketi_rs.items import AromaMarketiRsItemCoffee
from fake_useragent import UserAgent
ua = UserAgent()


class CoffeeSpider(scrapy.Spider):
    name = "coffee"
    # allowed_domains = ["."]
    # start_urls = ["https://."]
    def start_requests(self):
        url = "https://aromamarketi.rs/ponude/"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://aromamarketi.rs/',
            'User-Agent': ua.random
        }
        yield scrapy.Request(url, headers=headers, callback=self.parse_products)

    def parse_products(self, response):
        site_domain = 'https://aromamarketi.rs/'
        file_dir = f'C:/Users/Actowiz/Desktop/pagesave/aroma_marketi_rs/coffee_duplicates'
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        filename = fr'{file_dir}/pagesave.html'
        file = open(filename, 'w', encoding='utf8')
        file.write(response.text)
        file.close()
        all_products_path = response.xpath("//div[contains(@class,'module__articles_categories_browser__item')]")
        for product in all_products_path:
            product_name = product.xpath(".//h3[@class='module__articles_categories_browser__title']/text()").get()
            image = product.xpath(".//p[@class='module__articles_categories_browser__image']//span/img/@src").get()
            price = product.xpath(".//p[contains(@class,'module__articles_categories_browser__price')]/text()").get()
            currency = product.xpath(".//p[contains(@class,'module__articles_categories_browser__price')]//sup[@class='currency']/text()").get()
            country = 'Serbia'
            image_url = site_domain + image
            item = AromaMarketiRsItemCoffee()
            item['name'] = product_name
            item['price'] = price
            item['mrp'] = price
            item['country'] = country
            item['currency'] = currency
            item['image'] = image_url
            item['pagesave'] = filename
            item['url'] = 'https://aromamarketi.rs/ponude/#offer-box'
            yield item





if __name__ == '__main__':
    execute("scrapy crawl coffee".split())