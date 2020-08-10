import scrapy

class BlogSpider(scrapy.Spider):
    name = 'languagespider'
    start_urls = ['https://www.bankexamstoday.com/2019/06/countries-capital-currency-and-languages.html']

    def parse(self, response):
        for link in response.css('tr td:nth-child(4)'):
            yield {'language': link.css('td::text').extract_first()}