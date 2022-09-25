from wsgiref import headers
import scrapy

from ..items import StockScrapyItem

class StockSpider(scrapy.Spider):
    name = "mostactive"
    def start_requests(self):
        #urls = ['https://finance.yahoo.com/quote/AAPL?p=AAPL',]
        urls = ['https://finance.yahoo.com/most-active',]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_pages)

    def get_pages(self, response):
        count = str(response.xpath('//*[@id="fin-scr-res-table"]/div[1]/div[1]/span[2]/span').css('::text').extract())
        total_results = int(count.split()[-2])
        total_offsets = total_results // 25 + 1
        offset_list = [i * 25 for i in range(total_offsets)]
        for offset in offset_list:
            yield scrapy.Request(url=f'https://finance.yahoo.com/most-active?count=25&offset={offset}', callback=self.get_stocks)

    def get_stocks(self, response):
        stocks = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody//tr/td[1]/a').css('::text').extract()
        for stock in stocks:
            yield scrapy.Request(url = f'https://finance.yahoo.com/quote/{stock}?p={stock}', callback=self.parse)

    def parse(self, response):
        items = StockScrapyItem()

        items['stock_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').extract()
        items['intraday_price'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]').css('::text').extract()
        items['price_change'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[3]/span').css('::text').extract()

        yield items