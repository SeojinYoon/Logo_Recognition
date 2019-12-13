# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:26:02 2019

@author: Heo
"""
# 파일 읽어오기
with open("C:/yolo/colab_result.txt","r") as file:
    data = file.readlines()
    for i in data:
        print(i,end='')

data = data[4:] #맨앞에 필요없는 3줄 버리기
data
'''
['Start processing exp/in_images/google_asahi8.png\n',
 'exp/in_images/google_asahi8.png: Predicted in 8588.055000 milli-seconds.\n',
 'ASAHI: 62%\n',
 'End\n',
 'Start processing exp/in_images/google_kozel1.png\n',
 'exp/in_images/google_kozel1.png: Predicted in 8475.756000 milli-seconds.\n',
 'End\n',
 'Start processing exp/in_images/google_kirin_ichiban7.png\n',
 'exp/in_images/google_kirin_ichiban7.png: Predicted in 8449.032000 milli-seconds.\n',
 'KIRIN_ICHIBAN: 97%\n',
 'KIRIN_ICHIBAN: 91%\n',
 'KIRIN_ICHIBAN: 98%\n',
 'End\n',
 'Start processing exp/in_images/google_kloud5.png\n',
 'exp/in_images/google_kloud5.png: Predicted in 8523.221000 milli-seconds.\n',
 'KLOUD: 43%\n',
 'KLOUD: 62%\n',
 'KLOUD: 43%\n',
 'KLOUD: 47%\n',
 'End']
'''

# 결과값만
result = []
for i in data:
    if i.startswith('ASAHI') or i.startswith('KIRIN_ICHIBAN') or i.startswith('KLOUD') or i.startswith('End'):
        result.append(i)
result
'''
ASAHI: 62%
End
End
KIRIN_ICHIBAN: 97%
KIRIN_ICHIBAN: 91%
KIRIN_ICHIBAN: 98%
End
KLOUD: 43%
KLOUD: 62%
KLOUD: 43%
KLOUD: 47%
End
'''
# 사진별 결과값으로 분리
result_2=''
for i in result:
    result_2+=i

result_2
# 'ASAHI: 62%\nEnd\nEnd\nKIRIN_ICHIBAN: 97%\nKIRIN_ICHIBAN: 91%\nKIRIN_ICHIBAN: 98%\nEnd\nKLOUD: 43%\nKLOUD: 62%\nKLOUD: 43%\nKLOUD: 47%\nEnd'

result_3 = result_2.split('End')
result_3
'''
['ASAHI: 62%\n',
 '\n',
 '\nKIRIN_ICHIBAN: 97%\nKIRIN_ICHIBAN: 91%\nKIRIN_ICHIBAN: 98%\n',
 '\nKLOUD: 43%\nKLOUD: 62%\nKLOUD: 43%\nKLOUD: 47%\n',
 '']
'''

# 한 사진당 중복맥주 없이 count


len(result_3)-1 #총 결과값의 개수

for i in result_3:
    if i










'''
# 문자열로 변환
txt=''
for i in data:
    txt+=i

# 총 몇개의 결과값이 존재하는지 확인
print('총 ',txt.count('Start'),'개의 결과값이 있습니다')
# txt.count('End')


import re
re.match('\: \d+',txt)




# 결과값 분리하기
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[0]
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[1] #'\nASAHI: 62%\n'
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[2]
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[3]
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[7] #'\nKLOUD: 43%\nKLOUD: 62%\nKLOUD: 43%\nKLOUD: 47%\n'
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[8] 
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[9] #'\nASAHI: 62%\n'
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[10]
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[11]
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[12]
txt.replace('milli-seconds.','woojin').replace('End','woojin').split('woojin')[13] # '\nKIRIN_ICHIBAN: 97%\nKIRIN_ICHIBAN: 91%\nKIRIN_ICHIBAN: 98%\n'


for i in txt:
    i.replace('Start','woojin').split()



# 결과값 분리하기
txt.split('End')[0]
txt.split('End')[1]
txt.split('End')[2]
txt.split('End')[3]

data_split =[]
for i in range(txt.count('Start')+1):
    data_split.append(txt.split('Start')[i])

data_split=data_split[1:]

data_split_2=[]

for i in data_split:
    data_split.append(i.split('seconds'))






# 각각의 결과값 분리하기
s = txt.find('Start',0)
e = txt.find('End',0)
txt[s:e]

s = txt.find('Start',s+1)
e = txt.find('End',e+1)
txt[s:e]

result = []
for i in range(txt.count('Start')+1):
    s = txt.find('Start',s+1)
    e = txt.find('End',e+1)
    result.append(txt[s:e])
result[0]
result[1]
result[2]
result[3]
result[3][result[3].find('seconds.')+len('seconds.'):result[3].find('seconds.')+len('seconds.\n')+len('KLOUD')]


# 각 result에서 맥주 개수 카운트(중복 맥주는 1개로)
beer = ['ASAHI','BUDWEISSER','CASS','SAPPORO','TERRA','HEINEKEN',
        'HITE_EXTRACOLD','HOEGAARDEN','KIRIN_ICHIBAN','KRONENBOURG']

result
 
'''