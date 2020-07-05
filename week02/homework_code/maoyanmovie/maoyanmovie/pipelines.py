# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import pandas as pd


import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'vidian670',
    'db': 'test'
}


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']

        conn = pymysql.connect(
            host=dbInfo['host'],
            port=dbInfo['port'],
            user=dbInfo['user'],
            password=dbInfo['password'],
            db=dbInfo['db']
        )

        cur = conn.cursor()
        try:
            values = [movie_name, movie_type, movie_time]
            cur.execute('INSERT INTO  movie values(%s,%s,%s)', values)
            # 关闭游标
            cur.close()
            conn.commit()
        except Exception as e:
            print(f'error{e}')
            conn.rollback()
        conn.close()

        return item
