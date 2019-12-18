#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:41:39 2019

@author: yoonseojin
"""    

# YOLO Marker를 Mask Marker로 변환하는 코드

import os
import sys
sys.path.append('C:/Users/wdp/Documents/Logo_Recognition/workspace/Utility')
import imageUtil
from PIL import Image
import json

image_folder_path = 'C:/Users/wdp/Desktop/브랜드 이미지 (최종) (yolo 백업도 같이)/'

asahi_dic = make_mask_attribute_with_folder(image_folder_path + '0 ASAHI')
bud_dic = make_mask_attribute_with_folder(image_folder_path + '1 BUDWEISSER')
cass_dic = make_mask_attribute_with_folder(image_folder_path + '2 CASS')
sapporo_dic = make_mask_attribute_with_folder(image_folder_path + '3 SAPPORO')
terra_dic = make_mask_attribute_with_folder(image_folder_path + '4 TERRA')
heineken_dic = make_mask_attribute_with_folder(image_folder_path + '5 HEINEKEN')
hite_dic = make_mask_attribute_with_folder(image_folder_path + '6 HITE_EXTRACOLD')
hogaarden_dic = make_mask_attribute_with_folder(image_folder_path + '7 HOEGAARDEN')
kirin_dic = make_mask_attribute_with_folder(image_folder_path + '8 KIRIN_ICHIBAN')
kronen_dic = make_mask_attribute_with_folder(image_folder_path + '9 KRONENBOURG')

all_data_dics = [asahi_dic, bud_dic, cass_dic, sapporo_dic, terra_dic, heineken_dic, hite_dic, hogaarden_dic, kirin_dic, kronen_dic]

result_dic = {}
for data in all_data_dics:
    result_dic.update(data)
    
export_json(result_dic, 'c:/Users/wdp/Downloads/mask_marker_datas.json')

# 출력을 위한 함수 정의 ##################################################
def export_json(dictionary, export_file_path):
    with open(export_file_path, 'w') as f:
        f.write(json.dumps(dictionary))
# 출력을 위한 함수 정의 ##################################################
        
# yolo marking 을 mask로 바꾸기 위한 함수 정의 ##################################################
def make_mask_attribute_with_folder(yolo_marker_folder_path):
    image_paths = imageUtil.image_path(yolo_marker_folder_path)
    attrs = []
    for image_path in image_paths:
        attr = make_image_file_attribute(image_path)
        attrs.append(attr)
    
    dic = {}
    for attr in attrs:
        dic.update(attr)
    
    return dic
    
def make_image_file_attribute(image_file_path):
    yolo_bounding_txt_path = os.path.splitext(image_file_path)[0]+'.txt'
    with open(yolo_bounding_txt_path, 'r') as yolo_txt_file:
        image_size = get_image_size(image_file_path)
        image_width = image_size[0]
        image_height = image_size[1]
        region_attributes = []
        while(True):        
            line = yolo_txt_file.readline().replace("\n","")
            if line == '':
                break
            line_info = line.split(' ')
            class_name = int(line_info[0])
            x_center = float(line_info[1])
            y_center = float(line_info[2])
            width = float(line_info[3])
            height = float(line_info[4])
            rect = make_rect(x_center, y_center, width, height, image_width, image_height)
            class_rect = make_class_rect(class_name, rect)
            region_attributes.append(make_region_attribute(class_rect))
            
    image_file_name = get_file_name(image_file_path)
    file_size = get_file_size(image_file_path)
    return {
            image_file_name + str(file_size): {
                        "filename" : image_file_name,
                        "size" : file_size,
                        "regions" : region_attributes
                    }
            }

def make_region_attribute(class_rect):
    class_name = class_rect[0]
    if class_name == 0:
        class_name = 10 # 아사히의 경우 mask_rcnn은 클래스가 10임
    rect = class_rect[1]
    return {
            "shape_attributes" : {
                    "name" : "polygon",
                    "all_points_x" : [point[0] for point in rect],
                    "all_points_y" : [point[1] for point in rect]
                    },
            "region_attributes" : {
                    "logo" : str(class_name)
                    }
            }
            
def make_class_rect(class_value, rect_points):
    return (class_value, rect_points)
    
def make_rect(x_center, y_center, width, height, image_width, image_height):
    # <x_center> <y_center> <width> <height> - float values relative to width and height of image, it can be equal from (0.0 to 1.0]
    x_center_point = x_center * image_width
    y_center_point = y_center * image_height
    rect_width = width * image_width
    rect_height = height * image_height
    x1,y1 = x_center_point  - (0.5 * rect_width), y_center_point - (0.5 * rect_height)
    x2,y2 = x_center_point + (0.5 * rect_width), y_center_point - (0.5 * rect_height)
    x3,y3 = x_center_point + (0.5 * rect_width), y_center_point + (0.5 * rect_height)
    x4,y4 = x_center_point - (0.5 * rect_width), y_center_point + (0.5 * rect_height)
    
    if x1 < 0:
        x1 = 0
        
    if x4 < 0:
        x4 = 0
   
    if x2 > image_width:
        x2 = image_width
    
    if x3 > image_width:
        x3 = image_width
        
    if y1 < 0:
        y1 = 0
    
    if y2 < 0:
        y2 = 0
        
    if y3 > image_height:
        y3 = image_height
        
    if y4 > image_height:
        y4 = image_height
    
    return [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# yolo marking 을 mask로 바꾸기 위한 함수 정의 ##################################################
    
# file_helper_functions ##################################################
def get_file_name(file_path):
    return os.path.basename(file_path)

def get_file_size(file_path):
    return os.path.getsize(file_path)

def get_image_size(image_path):
    im = Image.open(image_path)
    width, height = im.size
    return (width, height)
# file_helper_functions ##################################################

