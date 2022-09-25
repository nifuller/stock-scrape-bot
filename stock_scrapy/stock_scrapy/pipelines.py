# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import XmlItemExporter
from itemadapter import ItemAdapter
import json

class XmlExportPipeline(object):
    def __init__(self):
        self.files = {}
        self.file = open('mostactive.xml', 'a')
        self.exporter = XmlItemExporter(self.file)
    
    def spider_opened(self, spider):
        file = open('mostactive.xml', 'a')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file, item_element='Most_Active', root_element='Most_Active')
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
class StockScrapyPipeline:
    def process_item(self, item, spider):
        return item
class JsonStockScrapyPipeline:
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file = open('mostactive.json', 'w')

    def close_spider(self, spider):
        self.file.close()