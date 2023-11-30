import scrapy, random, time
from ..items import NeweggItem

class NeweggGpuSpider(scrapy.Spider):
    name = 'newegg_gpu'
    start_urls = ['https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48']

    def parse(self, response):
        # Add random delay between requests
        delay = random.uniform(0.5, 2.0)  # Adjust the range as needed
        time.sleep(delay)
        for product in response.css('.item-container'):
            item = NeweggItem()
            item['ItemID'] = product.css('.item-number::text').get().strip()
            item['title'] = product.css('.item-title::text').get().strip()
            item['branding'] = product.css('.item-branding::text').get().strip()
            item['rating'] = product.css('.item-rating::text').get().strip()
            item['num_ratings'] = product.css('.item-rating-num::text').get().strip()
            item['price'] = product.css('.price.price::text').get().strip()
            item['shipping'] = product.css('.shipping-promo::text').get().strip()
            item['image_url'] = product.css('img::attr(src)').get()

            specs_mapping = {
                'Max Resolution': 'max_resolution',
                'DisplayPort': 'display_port',
                'HDMI': 'hdmi',
                'DirectX': 'direct_x',
                'Model': 'model'
            }

            specs = product.css('.item-features li::text').extract()

            for spec in specs:
                for label, field_name in specs_mapping.items():
                    if label in spec:
                        item[field_name] = spec.strip()
                        break

            yield item

        next_page = response.css('a.page-link.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)