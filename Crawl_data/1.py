import os
import csv
from sqlalchemy import create_engine
import tushare as ts
import pandas as pd
import pymysql
from pymysql.cursors import DictCursor

DB_CONFIG = {
    'host': '47.94.199.64',
    'port': 3306,
    'user': 'wyq',
    'password': 'wyqlm12345678',
    'db': 'stock',
    'charset': 'utf8'
}

def create_total():
    engine = create_engine("mysql+pymysql://wyq:wyqlm12345678@47.94.199.64/stock", encoding='utf-8')  # 用sqlalchemy创建引擎
    pro = ts.pro_api('a75a21e7da073704f83c8f55013847332ad70d7a1dd2f90197c5fa89')
    df = pro.stock_basic(list_status='L',
                           fields='ts_code,symbol,name,fullname,area,industry,list_status')  # 获得上市状态的股票列表，只取五个字段
    df.to_sql('all_company', engine, if_exists='append')
    #df.to_csv('实时行情数据.csv')

def git_code():
    conn = pymysql.Connect(**DB_CONFIG)
    cursor = conn.cursor()
    sql = 'select symbol from all_company'
    cursor.execute(sql)
    all_code = cursor.fetchall()
    for code in all_code:
        create_table(list(code)[0])\
        #create_csv(list(code)[0])
    conn.close()

def create_csv(code):
    try:
        df = ts.get_hist_data(code)
        df.to_csv('data_csv/'+code+'.csv')
    except:
        pass

def create_table(code):
    try:
        df = ts.get_hist_data(str(code))  # 读取数据，格式为DataFrame
        engine = create_engine("mysql+pymysql://wyq:wyqlm12345678@47.94.199.64/stock", encoding='utf-8')  # 用sqlalchemy创建引擎
        print('连接成功')
        df.to_sql(str(code), engine, if_exists='append')  # 存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么
    except:
        pass

if __name__ == '__main__':
    git_code()
    #create_total()