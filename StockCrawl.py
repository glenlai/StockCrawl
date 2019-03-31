#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:39:18 2019

@author: laiyiren
"""
import time
from pandas.core.frame import DataFrame
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime
import webbrowser 
import csv
import os
import codecs
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

#def loop_find():


def enter_stock_detail(m):#輸入欲查詢年份/月份/股票代號並取得網址
    #year = input('請輸入民國年:')
    year = 103
    month = m
    stock_num =2330
    
    year = int(year)+1911
    year = str(year)

    #month = int(input('請輸入月份'))
    month = ('%02d'%month) #以雙位數呈現月份
   
    #stock_num = input('請輸入股票代號')    
    
    my_params =  {'response':'html','date':year+month+'01','stockNo':stock_num}
    return my_params

def get_url(a_stirng):
    r = requests.get("http://www.twse.com.tw/exchangeReport/STOCK_DAY" , params = my_params)
    return r
    
    

def parser(a):
    soup = BeautifulSoup(r.text , 'html.parser')    
    sel = soup.select("body td")#把網頁標籤body中有td選出成為一list
    list1 = []
    
    for tags in sel:
        list1.append(tags.string)
    #將一維轉二維
    test = [[list1[i+9*j] for i in range(9)]for j in range (1,(int(len(list1)/9)))]

    return test
    

def to_gsheet(k):
    GDriveJSON = 'pytosheet.json'
    GSpreadSheet = 'crawl'
    waitsec = 0.2
    count = 0
    title=["日", '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
    try:
        scope = ['https://www.googleapis.com/auth/drive']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
        val = worksheet.cell(1, 2).value
        if val=='':
            worksheet.append_row(title)
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)
    
    while True:        
 
        worksheet.append_row(k[count])
        count = count+1
        print('新增一列資料到試算表' ,GSpreadSheet)
        if count == len(k):
            print("stop")
            break
        time.sleep(waitsec)

    
    return 0

time_start = time.time()
for i in range(1,13):
    num = 0
    my_params = enter_stock_detail(i)
    r =get_url(my_params)
    k = parser(r)
    print(len(k))
    num = num+len(k)
    to_gsheet(k)
time_end = time.time()

print("it costs %f sec" %(time_end-time_start))
print("total %d" %num)