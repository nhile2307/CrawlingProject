# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import csv

class NeweggPipeline:
    def open_spider(self, spider):
        self.csv_file = open('output.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=[
            'ItemID', 'title', 'branding', 'rating', 'num_ratings', 'price', 'shipping', 'image_url',
            'max_resolution', 'display_port', 'hdmi', 'direct_x', 'model', 'Total_Price'
        ])
        self.csv_writer.writeheader()

    def close_spider(self, spider):
        self.csv_file.close()

    def process_item(self, item, spider):
        total_price = float(item.get('price', 0)) + float(item.get('shipping', 0))

        self.csv_writer.writerow({
            'ItemID': item.get('ItemID'),
            'title': item.get('title'),
            'branding': item.get('branding'),
            'rating': item.get('rating'),
            'num_ratings': item.get('num_ratings'),
            'price': item.get('price'),
            'shipping': item.get('shipping'),
            'image_url': item.get('image_url'),
            'max_resolution': item.get('max_resolution'),
            'display_port': item.get('display_port'),
            'hdmi': item.get('hdmi'),
            'direct_x': item.get('direct_x'),
            'model': item.get('model'),
            'Total_Price': total_price  # Calculate Total Price as the sum of Price and Shipping
        })
        return item
