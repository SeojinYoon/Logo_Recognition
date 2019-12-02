# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:39:32 2019

@author: stu15
"""


import time 
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#GOOGLE
url = "https://www.google.com/?gws_rd=ssl"
driver = webdriver.Chrome("c:/data/chromedriVer.exe")
driver.get(url)

#검색어 창 선택
e = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")

#검색어 입력
e.send_keys("카스 후레쉬")

#엔터 입력
e.submit()

#이미지 항목 클릭
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()

#이미지의 스크롤을 내림
for i in range(1,50):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(3)

참고 :: 카스 후레쉬 이미지 자체가 얼마 없음

#해당 사이트 정보 저장
html = driver.page_source    
soup = BeautifulSoup(html,'html.parser')


#사이트 정보중 'img'의 'src' 주소만 추출
params = []
params2 = []

for i in soup.select('img'):
    if i.get('src') == None:
        None
    
    else :
        params.append(i['src'])
        

len(params)

#/IMAGE로 시작하는 FILE이 있어, 사진으로 가져오지 못해서 params2에 가능한 이미지 주소만 따로 저장        
for i in params:
    if i.startswith("data"):
        params2.append(i)
    elif i.startswith("https"):
        params2.append(i)
        
    if i.endswith("32x32.png"):
        None

len(params2)

#사진 데이터 저장   
x = 1
for i in params2:
    req.urlretrieve(i,"C:/data/TEAM_PROJECT/data/CASS FRESH/google_cass"+str(x)+".png")
    x += 1 


