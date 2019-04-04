#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:36:43 2019

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
from gspread_pandas import Spread, Client
from df2gspread import gspread2df as g2d
import matplotlib.pyplot as plt
import locale
import matplotlib
import matplotlib.ticker as ticker
matplotlib.matplotlib_fname()



def read_sheet():
    GDriveJSON = 'pytosheet.json'
    GSpreadSheet = 'crawl'
    try:
        scope = ['https://www.googleapis.com/auth/drive']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
        values_list = worksheet.row_values(1)
        if values_list!='':
            print(values_list)
            #worksheet.append_row(title)
            #df = sheet_to_df(worksheet)
            print("ok")
            sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR5F9VhZlgG46oZ9xWrztSJkoVLHlieoe6NjMod-jovRPJGTBGQ7PB97MDillb0tzUnBd3UXZf403vL/pub?output=csv'
            csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
            df = pd.read_csv(csv_export_url)
           
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)
    
    return df




def draw_pic(df):
    # 设置绘图风格
    plt.style.use('ggplot')
    # 设置中文编码和负号的正常显示
    plt.rcParams['font.sans-serif'] = 'STHeiti'
    plt.rcParams['axes.unicode_minus'] = False
    data = df
    row = len(data)
    ax = plt.gca()
    #ax1 = data.plot(kind='line',x='日',y='收盤價',color='red')
    fig, ax1 = plt.subplots()
    #print(data['成交股數'])
    data.plot(kind='line',x='日',y='收盤價',color='red',ax=ax1)
    ax2 = ax1.twinx()
    data.plot(kind='bar',x='日',y='成交股數',color='blue',ax=ax2)
    #plt.figure()
    return 0

    
def draw_test1(df):
    data = df
    fig, ax1 = plt.subplots()
    #ax1 = data.plot(kind='bar',x='日',y='收盤價',color='red')
    # 设置绘图风格
    #plt.style.use('ggplot')
    # 设置中文编码和负号的正常显示
    plt.rcParams['font.sans-serif'] = 'STHeiti'
    plt.rcParams['axes.unicode_minus'] = False
    
    
  
    color = 'tab:red'
    ax1.set_xlabel('成交日期')
    ax1.set_ylabel('股價', color=color)
    ax1.plot(data['日'],data['收盤價'], color='red')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    #ax2 = data.plot(kind='bar',x='日',y='成交股數',color='blue')
    color = 'tab:blue'
    ax2.set_ylabel('成交股數', color=color)  # we already handled the x-label with ax1
    ax2.plot(data['日'],data['成交股數'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    #print(type(fig))
    #print(type(ax1))
    #fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
    
def draw_test2(df):
    data = df
    # 设置中文编码和负号的正常显示
    plt.rcParams['font.sans-serif'] = 'STHeiti'
    plt.rcParams['axes.unicode_minus'] = False
    x = data['日']
    plt.figure(figsize=(300,400))
    y1 = data['收盤價']
    y2 = data['成交股數']
    
    fig,ax1 = plt.subplots()
    
    ax2 = ax1.twinx()
    
    ax1.plot(x,y1, color='red')
    ax1.set_xlabel('成交日期')
    
    #ax2.plot(x,y2,color='blue')
    #ax2.set_ylabel('成交量')
    every_nth = 28
    for n, label in enumerate(ax1.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    
    plt.show()
    
    
    

    
    
    
df = read_sheet()
draw_test2(df)
#print ((df))
#draw_pic(df)
