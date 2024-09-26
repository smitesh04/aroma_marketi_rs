# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from aroma_marketi_rs.items import AromaMarketiRsItemCoffee
from aroma_marketi_rs.db_config import  DbConfig
obj = DbConfig()

class AromaMarketiRsPipeline:
    def process_item(self, item, spider):
        if isinstance(item, AromaMarketiRsItemCoffee):
            qr = f'''
                        insert into {obj.data_with_duplicates_table}(name, url, currency, price, mrp, country, image, pagesave)
                        values(
                        "{item['name']}",
                        "{item['url']}",
                        "{item['currency']}",
                        "{item['price']}",
                        "{item['mrp']}",
                        "{item['country']}",
                        "{item['image']}",
                        "{item['pagesave']}"
                        )
                        '''
            try:
                obj.cur.execute(qr)
                obj.con.commit()
            except Exception as e:
                print(e)
        return item
