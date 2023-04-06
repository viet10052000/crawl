import scrapy


class FptshopSpider(scrapy.Spider):
    name = "fptshop"
    allowed_domains = ["fptshop.com.vn"]
    start_urls = ["http://fptshop.com.vn/dien-thoai"]

    def parse(self, response):
        product_names = response.xpath("//div[@class='cdt-product-wrapper']")
        print(product_names)
        for item_url in response.css("div.cdt-product__img > a ::attr(href)").extract():
            print(item_url)
            yield {
                'link' : response.urljoin(item_url),
            }
