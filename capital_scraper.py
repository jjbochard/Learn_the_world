import scrapy

class BlogSpider(scrapy.Spider):
    name = 'capitalspider'
    start_urls = ['https://www.bankexamstoday.com/2019/06/countries-capital-currency-and-languages.html']

    def parse(self, response):
        for link in response.css('tr td:nth-child(2)'):
            yield {'capital': link.css('td::text').extract_first()}

