import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://cn.bing.com"]

    def parse(self, response):
        print(response.text)
