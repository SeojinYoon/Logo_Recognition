# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:48:50 2019

@author: stu15
"""

import time 
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#GOOGLE
url = "https://search.naver.com/search.naver?sm=tab_sly.hst&where=image&query=&oquery=%EC%B9%B4%EC%8A%A4+%ED%94%84%EB%A0%88%EC%89%AC&tqi=UPgVWdp0YiRss4KGxfCsssssstR-161930"
driver = webdriver.Chrome("c:/data/chromedriVer.exe")
driver.get(url)

#검색어 창 선택
e = driver.find_element_by_id("nx_query")

#검색어 입력
e.send_keys("카스 프레쉬")

#엔터 입력
e.submit()


#이미지의 스크롤을 내림
for i in range(1,50):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(5)
    if i == 6:
        driver.find_element_by_xpath("//*[@id='_sau_imageTab']/div[2]/div[8]/a").click()

참고 :: 네이버는 6번째 루프에서 이미지 추가 버튼이 튀어나와서 스크롤이 안내려간다.
그래서 6번째에 if문으로 이미지 추가 버튼 누르도록 처리

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


#사진 데이터 저장   
x = 1
for i in params:
    req.urlretrieve(i,"C:/data/TEAM_PROJECT/data/CASS_FRESH/naver_cass"+str(x)+".png")
    x += 1 

#사진데이터 저장 코드 수정
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/CASS_LIGHT/"
    name="naver_cass_light"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
