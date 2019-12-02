# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:39:32 2019

@author: stu15
"""

import time
import urlib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selsnium.webdriver.common.keys import Keys

url = "https://www.google.com/search?q=%EC%B9%B4%EC%8A%A4+%EB%A1%9C%EA%B3%A0&safe=active&rlz=1C1OKWM_koKR853KR854&sxsrf=ACYBGNQK3gMl9xZMAUszKAvJGiye2aeQZA:1575276034130&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj91L_DyJbmAhXSMd4KHbQaBvoQ_AUoAXoECAoQAw&biw=1920&bih=888"
