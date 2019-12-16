#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:09:50 2019

@author: yoonseojin
"""
    
def write(file_path, message):
    with open(file_path, 'w') as file:
        file.write(message)

if __name__== "__main__":
    # python 파일을 import 하기 위한 경로 설정(각자의 경로의 맞게 설정 필요))
    import sys 
    sys.path.append('/Users/yoonseojin/Logo_Recognition/workspace/utility')
    
    # import
    import fileUtil
    
    # 에제
    write('/Users/yoonseojin/Desktop/test.txt', '이런이런!')
