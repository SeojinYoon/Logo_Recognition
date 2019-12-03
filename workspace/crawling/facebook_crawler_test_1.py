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

user = 'gjdnwlsdl@naver.com' # 아이디를 입력하세요
mypass = '_' #비밀번호를 입력하세요

#아이디 입력하는 곳
inputid = driver.find_element_by_name("email")
inputid.clear()
inputid.send_keys(user)

# 비밀번호 
inputpw=driver.find_element_by_name("pass")
inputpw.clear()
inputpw.send_keys(mypass)

# 로그인버튼
#loginbn=driver.find_element_by_name("login")
loginbn=driver.find_element_by_id("loginbutton") #사용환경마다 
loginbn.submit()

# 이전에 알림은 수동으로 '차단'버튼을 눌러줘야 한다.
# 키워드 입력
inputpw=driver.find_element_by_name("q")
inputpw.clear()
inputpw.send_keys("맥주")

# 엔터
keyword=driver.find_element_by_class_name("_585_")
keyword.submit()

# 사진 카테고리로 가기
# 아래 코드로 안들어가지면 손으로 클릭..
photo=driver.find_element_by_xpath('//*[@id="u_fetchstream_2_1"]/div/div/div/ul/li[4]/a').click()

## 날짜 선택
# 2018년 클릭하기
bn2018 = driver.find_element_by_xpath('//*[@id="u_ps_fetchstream_4_0_i"]/a[3]/label/span').click()
month = driver.find_element_by_xpath('//*[@id="u_ps_fetchstream_5_0_m"]').click()
july = driver.find_element_by_xpath('//*[@id="u_ps_fetchstream_5_0_9"]/div/ul/li[8]/a/span/span').click()

# 날짜선택 클릭 --> 2018년 7월

# 모두보기
allpic = driver.find_element_by_xpath('//*[@id="u_ps_fetchstream_9_3_4"]/div/a').click()

## 사진 하나씩 클릭 -> 사진, 날짜 가져오기 
# 사진 하나씩 클릭 ## 어떻게 해야하지..?
pic_click = driver.find_element_by_xpath('//*[@id="u_ps_fetchstream_6_3_n"]/a/div').click()

'//*[@id="u_ps_0_3_p"]/a/div/img'
'//*[@id="u_ps_0_3_u"]/a/div/img'
'//*[@id="u_ps_0_3_z"]/a/div/img'
'//*[@id="u_ps_0_3_14"]/a/div/img'
'//*[@id="u_ps_0_3_19"]/a/div/img'

# 사진 가져오기 
html = driver.page_source 
soup = BeautifulSoup(html,"html.parser")
imglink = soup.find_all("img",class_="spotlight")     
imgurl = []
for i in imglink:
    imgurl.append(i['src'])
imgurl

# 날짜 가져오기
day = soup.find("span",class_="timestampContent").get_text()
day_new = str(day[0:4])+str(day[6:8])+str(day[10:11])


# 이미지 컴퓨터에 저장
imgurl
for i in imgurl:
    dir = 'c:/facebook_beer_1807/'
    name = day_new
    req.urlretrieve(i,dir+name+'png')      #이미지 다운로드
    



# 닫기


'''
# 스크롤내리기
for i in range(1,5):             #스크롤을 내리는 작업을 4번 하겠다는 뜻
    driver.find_element_by_tag_name('body').send_keys(Keys.END) #스크롤을 끝까지 내리기
    time.sleep(5)

html=driver.page_source  #페이지 소스를 html에 저장
soup=BeautifulSoup(html,"html.parser")  #html 열기 

#이미지 url가 들어있는 태그와 class를 넣어 url들의 리스트를 imageurl에 저장
imgurl=[]   
imglink=soup.find_all("img",class_="scaledImageFitHeight img")     
for i in imglink:
    imgurl.append(i['src'])
    
imgurl  #이미지 url정보들이 저장됨

# 이미지 url들을 가지고 내 pc에 이미지 저장하기 
x=1
for i in imgurl:
    req.urlretrieve(i,"c:/beer/facebook_08july"+str(x)+".jpg")      #이미지 다운로드
    x += 1
'''
