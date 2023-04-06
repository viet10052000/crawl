import scrapy


class ViettelstoreSpider(scrapy.Spider):
    name = "viettelstore"
    allowed_domains = ["viettelstore.vn"]
    start_urls = ["http://viettelstore.vn/dien-thoai",
                  "https://viettelstore.vn/may-tinh-bang",
                  "https://viettelstore.vn/phu-kien/tai-nghe-pkid010005005.html"]

    def parse(self, response):
        for item_url in response.css("#div_Danh_Sach_San_Pham div.item > a ::attr(href)").extract():
            yield {
                'link' : response.urljoin(item_url),
            }
