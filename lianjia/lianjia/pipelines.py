# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from lianjia.items import  LianjiaItem
import json
import os
import csv


class LianjiaJsonPipeline(object):
    def __init__(self):
        dir_name = os.path.dirname(os.path.dirname(__file__))
        new_path = os.path.join(dir_name, "data")
        if not os.path.exists(new_path):
            os.mkdir(new_path)

        self.json_file = open(new_path + "/lianjia_zufang.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, LianjiaItem):
            content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
            self.json_file.write(content)
        return item

    def close_spider(self, spider):
        self.json_file.close()


class LianjiaCsvPipeline(object):
    def __init__(self):
        dir_name = os.path.dirname(os.path.dirname(__file__))
        new_path = os.path.join(dir_name, "data")
        if not os.path.exists(new_path):
            os.mkdir(new_path)

        self.csv_file = open(new_path + "/lianjia_zufang.csv", "w")
        self.csv_writer = csv.writer(self.csv_file)
        key_data = "address,price,address_detail,detail_url,area,floor,house_type,release_time,content".split(',')
        self.csv_writer.writerow(key_data)

    def process_item(self, item, spider):
        if isinstance(item, LianjiaItem):
            value_data = dict(item).values()
            self.csv_writer.writerow(value_data)
        return item

    def close_spider(self, spider):
        self.csv_file.close()
