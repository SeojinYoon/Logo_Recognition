# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:55:24 2019

@author: stu15
"""


import time 
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#INSTAGRAM
url = "https://www.instagram.com/explore/tags/%ED%8E%B8%EB%A7%A5/"
driver = webdriver.Chrome("c:/data/chromedriVer.exe")
driver.get(url)

#로그인 창 클릭
driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button").click()

#아이디 클릭
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").click()

e = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")

#아이디 입력
e.send_keys("jtax90")

#비번 클릭
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").click()

#비번 입력
e = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

e.send_keys("")

#엔터 입력
e.submit()


#사진 검색
params = []
time_t = []
params2 = []

#사진과 시간대 수집
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]").click()    
for i in range(1,1001):
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    
    params.append(soup.find_all('img',class_='FFVAD')[-1])
    time_t.append(soup.find("time",class_='_1o9PC Nzb55')['datetime'])

    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/a[2]").click()
    time.sleep(1)



#params에서 주소만 출력
for i in params:
    params2.append(i['src'])

len(params)
len(time_t)
len(params2)


#날짜를 조정
import re
time_t2 = []

for i in time_t:
    print(re.findall('....-..-..',i))
    time_t2.append(re.findall('....-..-..',i))


import pandas as pd
from pandas import pandas, DataFrame

X = pd.DataFrame(params2)
Y = pd.DataFrame(time_t2)

#주소와 사진 두가지를 변수에 담아서 concat

TEST = pd.concat([X,Y],axis=1)

import datetime

#TEST 컬럼 변경
TEST.columns = ['image','date']
TEST['date']

#특정 날짜만 출력
TEST_IMAGE = TEST[(TEST['date']>='2019-11-27')&(TEST['date']<='2019-11-30')]


#주소 데이터를 저장위치에 저장
x = 1
for i in TEST_IMAGE['image']:
    req.urlretrieve(i,"C:/data/sample/"+TEST['date'][x]+"_"+str(x)+".png")
    x += 1 


