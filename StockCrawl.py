#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:39:18 2019

@author: laiyiren
"""

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

def enter_stock_detail():
    year = input('請輸入西元年:')
    year = str(year)

    month = int(input('請輸入月份'))
    month = ('%02d'%month) #以雙位數呈現月份
   
    stock_num = input('請輸入股票代號')    
    
    
    
    
    
    
enter_stock_detail()