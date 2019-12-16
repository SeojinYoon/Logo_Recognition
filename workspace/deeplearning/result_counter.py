# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:26:02 2019

@author: Heo
"""
from collections import Counter
import re

# 파일 읽어오기
with open("C:/yolo/colab_result.txt","r") as file:
    data = file.readlines()
    for i in data:
        print(i,end='')

#맨앞에 필요없는 3줄 버리기
data = data[4:] 


# 사진별 결과값으로 분리
result_1=''
for i in data:
    result_1+=i
    
result_1 = result_1.split('End')


# 한 사진당 중복맥주 없이 count
result_2=[]
for i in result_1:
    result_2.append(re.findall('[A-Z]+\:',i))
    
result_2 = result_2[:-1] #맨 마지막의 의미없는 줄 지우기


# 리스트 내에서 중복제거 함수 만들기
def uniq(aList):
    return [x for i, x in enumerate(aList) if x not in aList[:i]]


# 각 사진별 맥주 종류(중복 맥주는 하나만)
beer_in_pic=[]
for i in result_2:
    beer_in_pic.append(uniq(i))

beer_in_pic


# 전체 값 count하기
result_3 = sum(beer_in_pic,[])
total_beer = Counter(result_3)
total_beer
