import scrapy
 
 
class GdpDebtSpider(scrapy.Spider):
    name = "gdp_debt"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/country-list/government-debt-to-gdp"]
 
    def parse(self, response):
        rows = response.xpath("//table//tr")
        for row in rows:
            country_name = row.xpath(".//td[1]/a").xpath("normalize-space()").get()
            gdp_debt = row.xpath(".//td[2]/text()").get()
            yield {
                "country_name": country_name,
                "gdp_debt": gdp_debt,
            }
 