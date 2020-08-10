import scrapy

class BlogSpider(scrapy.Spider):
    name = 'countryspider'
    start_urls = ['https://www.bankexamstoday.com/2019/06/countries-capital-currency-and-languages.html']

    def parse(self, response):
        for link in response.css('tr td:nth-child(1)'):
            yield {'country': link.css('strong::text').extract_first()}

