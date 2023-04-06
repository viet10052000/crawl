import scrapy


class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ["shopee.vn"]
    start_urls = ["https://shopee.vn/search?keyword=%C4%91i%E1%BB%87n%20tho%E1%BA%A1i&order=desc&page=0&sortBy=price&trackingId=searchhint-1680539189-49f51c47-d23c-11ed-a43e-3473791712f2"]

    def parse(self, response):
        for item_url in response.css("div.shopee-search-item-result__items div.shopee-search-item-result__item > a ::attr(href)").extract():
            yield {
                'link' : response.urljoin(item_url),
            }
