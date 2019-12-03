# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:40:59 2019

@author: stu15
"""
import time 
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#NAVER
url = "https://www.google.com/search?safe=active&tbm=isch&q=%E9%9D%92%E5%B2%9B%E5%95%A4%E9%85%92&chips=q:%E9%9D%92%E5%B2%9B+%E5%95%A4%E9%85%92,online_chips:tsingtao+beer&sa=X&ved=0ahUKEwjSoKn1rZnmAhVQc3AKHe66COgQ4lYIKigB&biw=929&bih=884&dpr=1"
driver = webdriver.Chrome("c:/data/chromedriVer.exe")
driver.get(url)

#검색어 창 선택
e = driver.find_element_by_id("nx_query")

#검색어 입력
e.send_keys("카스 후레쉬")
e.send_keys("카스 라이트")
e.send_keys("하이트 맥주")
e.send_keys("하이네켄")
e.send_keys("호가든")
e.send_keys("아사히 맥주")
e.send_keys("버드와이저")
e.send_keys("기린 이치방 맥주")
e.send_keys("클라우드 맥주")
e.send_keys("코젤")
e.send_keys("삿뽀로 맥주")
e.send_keys("필스너 우르켈")
e.send_keys("크로넨버그 맥주")
e.send_keys("스텔라 아르투아")
e.send_keys("테라 맥주")
e.send_keys("칭다오 맥주")


#엔터 입력
e.submit()


#이미지의 스크롤을 내림
for i in range(1,50):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(3)
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


#사진데이터 저장 코드 수정/추가 -> 자동화필요
#경로(dir) 맨끝에 / 붙여줄것
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/CASS_FRESH/"
    name="naver_cass_fresh"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/CASS_LIGHT/"
    name="naver_cass_light"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/HEINEKEN/"
    name="naver_heineken"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/HITE/"
    name="naver_hite"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/HOEGAARDEN/"
    name="naver_hoegaarden"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/ASAHI/"
    name="naver_asahi"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/BUDWEISSER/"
    name="naver_budweisser"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/KIRIN_ICHIBAN/"
    name="naver_kirin_ichiban"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/KLOUD/"
    name="naver_kloud"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/KOZEL/"
    name="naver_kozel"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1    


x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/KRONENBOURG/"
    name="naver_kronenbourg"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1    
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/PILSNER_URQUELL/"
    name="naver_pilsner_urquell"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1    
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/SAPPORO/"
    name="naver_sapporo"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1   

x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/STELLA_ARTOIS/"
    name="naver_stella_artois"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/TERRA/"
    name="naver_terra"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
params = params[:-3]
for i in params:
    if i == '/tia/tia.png' :
        None
    else:
        params2.append(i)

x = 1
for i in params:
    dir="C:/data/TEAM_PROJECT/data/TSINGTAO/"
    name="baidu2_tsingtao"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
