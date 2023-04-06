import scrapy
from shoponline.items import ProductItem

class ThegioididongDtddSpider(scrapy.Spider):
    name = "thegioididong"
    allowed_domains = ["www.thegioididong.com"]
    start_urls = ["https://www.thegioididong.com/dtdd-apple-iphone",
                  "https://www.thegioididong.com/dtdd-samsung",
                  "https://www.thegioididong.com/dtdd-xiaomi",
                  "https://www.thegioididong.com/dtdd-vivo",
                  "https://www.thegioididong.com/dtdd-realme",
                  "https://www.thegioididong.com/dtdd-vivo",
                  "https://www.thegioididong.com/dtdd-oppo"]
                #   "https://www.thegioididong.com/laptop",
                #   "https://www.thegioididong.com/may-tinh-bang",
                #   "https://www.thegioididong.com/tai-nghe"]

    def parse(self, response):
        for item_url in response.css("ul.listproduct li.item > a.main-contain ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_product)

    def parse_product(self, response):
        item = ProductItem()
        
        item['category_id'] = response.css('section ::attr(data-cate-id)').extract_first()
        item['product_id'] = response.css('section ::attr(data-id)').extract_first()
        item['product_name'] = response.css('section.detail > h1 ::text').extract_first()
        price = response.css('div.price-one > div.box-price > p.box-price-old ::text').extract_first()
        if price :
            item['price'] = price
        else:    
            item['price'] = response.css('div.price-two > div.box-price > p.box-price-old ::text').extract_first()
            
        price_sale = response.css('div.price-one > div.box-price > p.box-price-present ::text').extract_first()  
        if price_sale :
            item['price_sale'] = price_sale
        else:    
            item['price_sale'] = response.css('div.price-two > div.box-price > p.box-price-present ::text').extract_first()   

        item['link_url'] = response.css('div.like-fanpage::attr(data-url)').extract_first()
        item['link_image'] = response.css('a.slider-item img::attr(src)').extract_first()
        
        yield item
