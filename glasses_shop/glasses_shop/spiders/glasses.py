import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath("//div[@id='product-lists']/div"):
            yield {
                'name' : product.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(),
                'product_price' : product.xpath(".//div[@class='p-price']//span[1]/text()").get(),
                'product_url' : product.xpath(".//div[@id='product-lists']/div//div[@class='p-title']/a[1]/@href").get(),
                'product_image' : product.xpath(".//div[@id='product-lists']/div//div[@class='product-img-outer']/a[1]/@href").get()
            }

        next_page = response.xpath("//a[@rel='next']/@href").get()

        if next_page:
            scrapy.Request(url=next_page, callback=self.parse)