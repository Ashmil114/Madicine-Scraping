from dotenv import load_dotenv
import os

# from itemadapter import ItemAdapter
import psycopg2

load_dotenv()


class CorePipeline:
    def process_item(self, item, spider):
        return item


class PostgresPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        # print(
        #     "==========================================",
        #     os.getenv("HOST"),
        #     os.getenv("DATABASE"),
        #     os.getenv("PG_USER"),
        #     os.getenv("PASSWORD"),
        #     "==========================================",
        # )
        self.conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PASSWORD"),
        )
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(
            """INSERT INTO tb_medicine (name, usage) VALUES (%s, %s)""",
            (item["name"], item["usage"]),
        )
        self.conn.commit()
