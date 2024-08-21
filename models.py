from peewee import *
import os
from dotenv import load_dotenv 

load_dotenv()

pg_db = PostgresqlDatabase('verceldb', user=os.getenv("USER"), password=os.getenv("PASSWORD"),
                        host=os.getenv("HOST"), port=5432)

class BaseModel(Model):
    class Meta:
        database = pg_db

class Product(BaseModel):
    product_id = AutoField(column_name='product_id')
    product_name = CharField(column_name='product_name', max_length=255, null=False)
    product_description = CharField(column_name='product_description', max_length=1000, null=False)
    product_price = IntegerField(column_name='product_price', null=False)

    class Meta:
        table_name = 'products'
