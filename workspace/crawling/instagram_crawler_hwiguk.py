# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:36:30 2019

@author: sty13
"""


# 인스타 웹 스크래핑
from selenium import webdriver
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

id_var = 'punkrocks1@naver.com' # 아이디
#pass_var = input('비밀번호를 입력 : ') # 비밀번호
search_var = '#편맥' # 키워드 검색
image_var = [] # 이미지 넣을 변수
date_var = [] # 날짜 넣을 변수
count_var = 1000 # 웹 스프래팅 개수 설정

# 최신 사진
# 인스타 접속
#url = "https://www.instagram.com/explore/tags/%ED%8E%B8%EB%A7%A5/?hl=ko"
url = "https://www.instagram.com/?hl=ko"
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.implicitly_wait(3)
driver.get(url)
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
#time.sleep(3)

# 인스타 로그인
#id_var = 'punkrocks1@naver.com' # 아이디
pass_var = input('비밀번호를 입력 : ') # 비밀번호

driver.implicitly_wait(5)
driver.find_element_by_name('username').send_keys(id_var)
driver.find_element_by_name('password').send_keys(pass_var)

driver.find_element_by_css_selector("button").submit()

time.sleep(3)
driver.implicitly_wait(50)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click() # 팝업 알림 나중에 하기 설정

# 키워드 검색 (#편맥, #캔맥)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div').click()

#search_var = '#편맥' # 키워드 검색
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(search_var)

driver.find_element_by_class_name('z556c').click()

# 웹 스크래핑
driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > a > div').click() # 첫번째 사진 클릭

for i in range(count_var):
    
    time.sleep(1.8) 
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    
    if soup.select_one('.fXIG0') != None: # 영상일 경우
        pass
    elif soup.select_one('.YlNGR') != None: # 여러장일 경우
        pass
    elif soup.select_one('.xUdfV') != None: # 예외일 경우
        pass
    else:
        image_var.append(soup.select_one('body > div._2dDPU.vCf6V > div.zZYga > div > article > div._97aPb > div > div > div.KL4Bh > img').attrs['src']) # 이미지
        date_var.append(soup.select_one('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > div.k_Q0X.NnvRN > a > time').attrs['title']) # 날짜
    
    driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.EfHg9 > div > div > a.HBoOv.coreSpriteRightPaginationArrow').click()

len(image_var) # 이미지 데이터
len(date_var) # 날짜 데이터

driver.quit()

x = 1 
for p in image_var: # 상품 리스트 이미지를 sample 폴더로 다운로드
    req.urlretrieve(p,"c:/sample/" + str(x) + ".jpg") 
    x += 1


x = 1
with open('c:/sample/date.txt','w') as f: # 상품 리스트 날짜를 sample 폴더로 다운로드
    for d in date_var:
        data = '%s,%s\n'%(x,d)
        print(data)
        f.write(data)
        x += 1

