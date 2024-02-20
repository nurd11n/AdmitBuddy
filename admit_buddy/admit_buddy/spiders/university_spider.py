import scrapy


class UniversityspiderSpider(scrapy.Spider):
    name = "UniversitySpider"
    allowed_domains = ["www.niche.com"]
    start_urls = ["https://www.niche.com/colleges/search/best-colleges/"]

    def parse(self, response):
        universities = response.xpath("//ol[@class='search-result__list']/li")
        for unik in universities:
            yield {
                # 'title': unik.xpath(".//[@class='search-result']/[@class='card']/h2[@class='MuiTypography-root MuiTypography-titleMedium MuiLink-root MuiLink-underlineHover nss-w5w7xf']/text()").get(),
                # 'top': unik.xpath(".//div[@class='MuiTypography-root MuiTypography-subtitle2 search-result-badge nss-tcks16']/text()").get()
                'href': unik.xpath(".//div[@class='card']/a/@href").get()
            }