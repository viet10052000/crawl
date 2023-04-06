import scrapy
from shoponline.items import ProductItem

class CellphonesSpider(scrapy.Spider):
    name = "cellphones"
    allowed_domains = ["cellphones.vn"]
    start_urls = ["https://cellphones.com.vn/mobile.html",
                  "https://cellphones.com.vn/laptop.html",
                  "https://cellphones.com.vn/tablet.html",
                  "https://cellphones.com.vn/thiet-bi-am-thanh.html",
                  "https://cellphones.com.vn/do-choi-cong-nghe.html"]

    def parse(self, response):
        for item_url in response.css("div.product-list-filter div.product-item div.product-info > a ::attr(href)").extract():
            yield {
                'link' : item_url
            }
            # yield scrapy.Request(response.urljoin(item_url), callback=self.parse_product)

    # def parse_product(self, response):
    #     item = ProductItem()
        
    #     item['category_id'] = ''
    #     item['product_id'] = ''
    #     item['product_name'] = response.css('div.box-product-name h1::text').extract_first()
    #     price = response.css('div.box-info__box-price > p.product__price--through ::text').extract_first()
    #     item['price'] = price
            
    #     price_sale = response.css('div.box-info__box-price > p.product__price--show ::text ::text').extract_first()  
    #     item['price_sale'] = price_sale 

    #     item['link_url'] = ''
    #     item['link_image'] = response.css('div.box-ksp img::attr(src)').extract_first()
        
    #     yield item
    
