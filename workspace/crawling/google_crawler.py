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

#이미지 항목 클릭
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()

#두번째로 지도 항목이 나타나는 경우, 세번째 이미지항목 클릭(아사히맥주)
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[3]/a').click()


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

#사진데이터 저장 코드 수정/추가 -> 자동화필요
#경로(dir) 맨끝에 / 붙여줄것  

x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/CASS_FRESH/"
    name="google_cass_fresh"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/CASS_LIGHT/"
    name="google_cass_light"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/HEINEKEN/"
    name="google_heineken"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/HITE/"
    name="google_hite"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/HOEGAARDEN/"
    name="google_hoegaarden"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/ASAHI/"
    name="google_asahi"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/BUDWEISSER/"
    name="google_budweisser"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/KIRIN_ICHIBAN/"
    name="google_kirin_ichiban"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/KLOUD/"
    name="google_kloud"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/KOZEL/"
    name="google_kozel"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1    


x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/KRONENBOURG/"
    name="google_kronenbourg"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1    
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/PILSNER_URQUELL/"
    name="google_pilsner_urquell"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1    
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/SAPPORO/"
    name="google_sapporo"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1   

x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/STELLA_ARTOIS/"
    name="google_stella_artois"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/TERRA/"
    name="google_terra"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 
    
    
x = 1
for i in params2:
    dir="C:/Users/stu20/Documents/Logo_Recognition/data/TSINGTAO/"
    name="google_tsingtao"
    req.urlretrieve(i,dir+name+str(x)+'.png')
    x += 1 

