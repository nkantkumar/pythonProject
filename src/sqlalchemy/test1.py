from MySQLdb.constants.FIELD_TYPE import VARCHAR, FLOAT
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, TIMESTAMP
import pandas as pd
engine = create_engine("mysql://root:@localhost/interview",echo = True)
metadata = MetaData()
conn = engine.connect()
'''
Student = Table('sales', metadata,
              Column('Id', Integer(),primary_key=True),
              Column('product_code', Integer()),
              Column('product_group', String(255)),
              Column('stock_qty', String(255)),
              Column('cost', String(255)),
              Column('price', String(255)),
                Column('last_week_sales', String(255)),
                Column('last_month_sales', String(255))
              )
metadata.create_all(engine)
'''
content = pd.read_csv('sales.csv')
table_name = 'sales'
content.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False)


pd.read_table