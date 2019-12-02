# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:31:15 2019

@author: stu21
"""

from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


url = 'https://www.facebook.com/'
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.implicitly_wait(3)
driver.get(url)    

user = '-' # 아이디를 입력하세요
mypass = '-' #비밀번호를 입력하세요

#아이디 입력하는 곳
inputid = driver.find_element_by_name("email")
inputid.clear()
inputid.send_keys(user)

# 비밀번호 
inputpw=driver.find_element_by_name("pass")
inputpw.clear()
inputpw.send_keys(mypass)

# 로그인버튼
loginbn=driver.find_element_by_name("login")
#loginbn=driver.find_element_by_id("loginbutton") 사용환경마다 
loginbn.submit()

# 키워드 입력
inputpw=driver.find_element_by_name("q")
inputpw.clear()
inputpw.send_keys("맥주")

# 엔터
keyword=driver.find_element_by_class_name("_585_")
keyword.submit()

# 사진 카테고리로 가기
#photo=driver.find_element_by_class_name("")
#photo.submit()
from selenium.webdriver.support.ui import WebDriverWait
WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="u_fetchstream_7_1"]/div/div/div/ul/li[4]/a/div/div[1]'))).click()
