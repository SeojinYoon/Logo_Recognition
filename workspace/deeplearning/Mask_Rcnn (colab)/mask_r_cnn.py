# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:01:44 2019

@author: sty13
"""

# * 텐서플로우하고 케라스가 이미 설치되어 있으면 skip
# 아나콘다 프롬프트를 관리자 권한으로 실행 후 아래 명령어를 실행하여 설치
# conda install tensorflow==1.14.0
# conda install keras


# 주피터에서 실행되는 소스코드를 가져와 실행했음 (inspect_balloon_model.ipynb 파일)
import os
import sys
import random
import math
import re
import time
import numpy as np
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# Root directory of the project
ROOT_DIR = "C:\\data\\Mask_RCNN (colab)" # 가끔 선언이 안될 때가 있어서 따로 이것만 실행
os.chdir('C:\\data\\Mask_RCNN (colab)') # mrcnn 를 import 하기위한 workspace path 설정

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log
from samples.Logo import Logo

%matplotlib inline 


# Directory to save logs and trained model
MODEL_DIR = ROOT_DIR + "\\samples\\mask_rcnn_logo_20000_(yolo_convert_6600).h5" # 가중치를 사용하는 모델 실제 경로 (.h5 파일은 모델 아키텍처와 모델 가중치로 구성되어 있다)


# Path to Ballon trained weights
# You can download this file from the Releases page6
# https://github.com/matterport/Mask_RCNN/releases
weights_path = ROOT_DIR + "\\samples\\mask_rcnn_logo_20000_(yolo_convert_6600).h5"  # 가중치 경로 (.h5 파일은 모델 아키텍처와 모델 가중치로 구성되어 있다)
print(ROOT_DIR) # 경로확인
print(MODEL_DIR) # 경로확인
print(weights_path) # 경로확인

# * Configurations
config = Logo.LogoConfig() # 환경설정 객체 생성
Logo_DIR = ROOT_DIR + "\\samples\\Logo\\logo_dataset_"
print(Logo_DIR)

# Override the training configurations with a few
# changes for inferencing.
class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig() # 환경설정 객체 생성
config.display() # 환경설정 출력

# * Notebook Preferences
# Device to load the neural network on.
# Useful if you're training a model on the same 
# machine, in which case use CPU and leave the
# GPU for training.
DEVICE = "/gpu:0"  # /cpu:0 or /gpu:0

def get_ax(rows=1, cols=1, size=16): # plot 출력하는 객체를 리턴하는 함수인듯
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.
    
    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

# * Load Validation Dataset
# Load validation dataset
dataset = Logo.LogoDataset() # 데이터셋 객체 생성
dataset.load_Logo(Logo_DIR, "val") # 검증 데이터셋 로드

# Must call before using the dataset
dataset.prepare()

print("Images: {}\n Classes: {}".format(len(dataset.image_ids), dataset.class_names))
print(Logo_DIR)


# * Load Model
# Create model in inference mode
with tf.device(DEVICE): # 모델 생성
    model = modellib.MaskRCNN(mode="inference", 
                              model_dir = MODEL_DIR,
                              config = config)
print(MODEL_DIR)

# Set path to Logo weights file

# Download file from the Releases page and set its path
# https://github.com/matterport/Mask_RCNN/releases
# weights_path = "/path/to/mask_rcnn_Logo.h5"

# Load weights
print("Loading weights ", weights_path)
model.load_weights(weights_path, by_name=True) # 가중치 로드
print(weights_path)


# * Run Detection
image_id = random.choice(dataset.image_ids) # 검증 데이터셋 폴더에서 임의의 이미지 인덱스 추출
image, image_meta, gt_class_id, gt_bbox, gt_mask = modellib.load_image_gt(dataset, 
                                                                          config, 
                                                                          image_id, 
                                                                          use_mini_mask=False)
info = dataset.image_info[image_id]
print("image ID: {} 다음 {} 다음 ({}) 다음 {}".format(info["source"], # 검증 데이터 이미지 정보 확인
                                                     info["id"],
                                                     image_id, 
                                                     dataset.image_reference(image_id)))


# Run object detection
results = model.detect([image], verbose=1) # 객체 탐지 

# Display results
ax = get_ax(1)
r = results[0] # 탐지된 객체 정보
ax = visualize.display_instances(image, 
                            r['rois'], 
                            r['masks'], 
                            r['class_ids'], 
                            dataset.class_names, 
                            r['scores'], 
                            ax=ax,
                            title="Logo Predictions")
print(r['class_ids']) # 클래스 넘버 (0 부터 시작이기에 + 1 이 됨)
print(r['rois']) # bounding box
log("gt_mask", r['masks']) # masking 영역


# * Color Splash
splash = Logo.color_splash(image, r['masks'])
display_images([splash], cols=1)



# 테스트 용 ==========================================
import skimage.io
os.chdir('C:/data/Mask_RCNN (colab)/samples') # 이미지가 있는 폴더 경로 설정
image = skimage.io.imread('sample2.jpg')
# 테스트 용 ==========================================



# * 원래 방법
# 이미지 폴더에서 임의의 이미지를로드
import skimage.io
os.chdir('C:/data/Mask_RCNN (colab)/samples') # 이미지가 있는 폴더 경로 설정
image = skimage.io.imread('sample2.jpg')

plt.figure(figsize=(12,10))
skimage.io.imshow(image)

# * 내가 수정한 방법 ( (1024,1024,3) 처럼 RGB 모양이 되야하는데 내 컴퓨터에서는 (1024,1024,4) 이런식으로 sRGB? 으로 표시되기에 Image 클래스를 사용하여 RGB 로 convert 하였음 ) 
# 임의의 이미지 하나만 테스트해보고자 할 경우, RGB 가 4 일 경우 detection 을 위해 이미지를 3 으로 변환해야 할 경우
from PIL import Image
os.chdir('C:/data/Mask_RCNN (colab)/samples')

image = Image.open('sample9.jpg')
plt.figure(figsize=(12,10))
plt.imshow(image)

image = image.convert("RGB")
image = np.array(image)
image.shape



# 모델에서 예측한 모든 마스크를 가져와서 마스크 변수에 저장
mask = r['masks'] # bool 형식
mask = mask.astype(int) # 숫자 형식 (0 과 1) 로 변환
mask.shape # (height, width, class count) 여기서 3번째 열은 모델에 의해 검출된 객체 수이다.
# 여기서 0 은 특정 픽셀에 객체가 없음을 의미하고 1 은 해당 픽셀에 객체가 있음을 의미한다. 마스크의 모양은 원본 이미지의 모양과 비슷함.



# 데이터셋의 내용 확인을 위한 소스코드
dataset.class_from_source_map
dataset.class_ids
dataset.class_info
dataset.class_names
dataset.image_from_source_map
dataset.image_info
dataset.num_classes
dataset.num_images
dataset.source_class_ids
dataset.sources
dataset.__doc__
dataset._image_ids



# logo count (페이스북 데이터 사진) (중복제거)
import skimage.io
import sys
import pandas as pd
sys.path.append('C:/data/Mask_RCNN (colab)/samples/Logo/Utility') # 유틸리티 경로 추가

import imageUtil
imagename_list = imageUtil.image_path('C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/val') # 이미지가 있는 폴더 경로 설정

image_name = []
logo_count = []
#x = 0 # x 번 이미지까지 나오는지 테스트를 위한 변수
for e in imagename_list:
    image = skimage.io.imread(e)
    
    # Run object detection
    result = model.detect([image], verbose=1) # 객체 탐지 
    
    print("result[0]['class_ids'] : " + str(result[0]['class_ids'])) # [5, 5]
    
    if type(result[0]['class_ids']) == np.ndarray:
        
        result[0]['class_ids'] = list(result[0]['class_ids'])
        result[0]['class_ids'] = pd.Series(result[0]['class_ids']).unique()
        
        for e in result[0]['class_ids']:
            logo_count.append(e)

#    image_name.append(e.split('/')[-1])

#    x += 1
#    if x == 19:
#        break

import collections
logo_count_list = str(collections.Counter(logo_count))

logo_count_list = logo_count_list.replace('Counter','')
logo_count_list = logo_count_list.replace('({','')
logo_count_list = logo_count_list.replace('})','')
logo_count_list = logo_count_list.replace(', ','\n')
        
with open("C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/results/logo_count_facebook_1909.txt","w") as fw:
    fw.write(logo_count_list)



# logo count (인스타 데이터 사진) (중복허용)
import skimage.io
import sys
import pandas as pd
sys.path.append('C:/data/Mask_RCNN/samples/Logo/Utility') # 유틸리티 경로 추가

import imageUtil
imagename_list = imageUtil.image_path('C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/val') # 이미지가 있는 폴더 경로 설정

logo_count = []
#x = 0 # x 번 이미지까지 나오는지 테스트를 위한 변수
for e in imagename_list:
    image = skimage.io.imread(e)
    
    # Run object detection
    result = model.detect([image], verbose=1) # 객체 탐지 
    
    print("result[0]['class_ids'] : " + str(result[0]['class_ids'])) # [5, 5]
    
    if type(result[0]['class_ids']) == np.ndarray:
        
        result[0]['class_ids'] = list(result[0]['class_ids'])
#        result[0]['class_ids'] = pd.Series(result[0]['class_ids']).unique()
        
        for e in result[0]['class_ids']:
            logo_count.append(e)
#    x += 1
#    if x == 19:
#        break

import collections
logo_count_list = str(collections.Counter(logo_count))

logo_count_list = logo_count_list.replace('Counter','')
logo_count_list = logo_count_list.replace('({','')
logo_count_list = logo_count_list.replace('})','')
logo_count_list = logo_count_list.replace(', ','\n')
        
with open("C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/results/logo_count_instagram.txt","w") as fw:
    fw.write(logo_count_list)



# 이미지 정보 리스트 텍스트 파일로 만들기1 (처음 만든부분) (무의미) (결과물 의미 순서 : 이미지 이름명, 로고 인덱스, 예측정확도)
import skimage.io
import sys
import pandas as pd
import collections
sys.path.append('C:/data/Mask_RCNN/samples/Logo/Utility') # 유틸리티 경로 추가

import imageUtil
imagename_list = imageUtil.image_path('C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/val') # 이미지가 있는 폴더 경로 설정

image_info_list = []

#for i in range(97):
for e in imagename_list:
    
    image = skimage.io.imread(e)
    
    # Run object detection
    result = model.detect([image], verbose=1) # 객체 탐지 
    
#    image_info_list.append(str(str(e.split('/')[-1]) + '  ' + str(result[0]['class_ids'])+ '  ' + str(result[0]['scores']) + '  ' + str(result[0]['rois']) + '  ' + '\n'))
    image_info_list.append(str(str(e.split('/')[-1]) + '  ' + str(result[0]['class_ids'])+ '  ' + str(result[0]['scores']) + '\n'))
    
image_info_list_str = ''
for e in image_info_list :
    image_info_list_str += e

with open("C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/results/image_info_list.txt","w") as fw:
    fw.write(image_info_list_str)



# 이미지 정보 리스트 텍스트 파일로 만들기2 (이미지 파일별 탐지 카운트)
import skimage.io
import sys
import pandas as pd
import collections
from pandas import DataFrame
sys.path.append('C:/data/Mask_RCNN/samples/Logo/Utility') # 유틸리티 경로 추가

import imageUtil
imagename_list = imageUtil.image_path('C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/val') # 이미지가 있는 폴더 경로 설정

image_info_name = []
image_info_counter = []
image_info_score = []

#for i in range(97):
for e in imagename_list:
    
    image = skimage.io.imread(e)
    
    # Run object detection
    result = model.detect([image], verbose=1) # 객체 탐지 
    
#    image_info_list.append(str(str(e.split('/')[-1]) + '  ' + str(result[0]['class_ids'])+ '  ' + str(result[0]['scores']) + '  ' + str(result[0]['rois']) + '  ' + '\n'))
#    image_info_list.append(str(str(e.split('/')[-1]) + '  ' + str(result[0]['class_ids'])+ '  ' + str(result[0]['scores']) + '\n'))
    
    image_info_name.append(e.split('/')[-1])
    counter = []
    score = []
    for i in result[0]['class_ids']:
        if i == 1:
            counter.append('BUDWEISSER ')
            score.append(result[0]['scores'])
        elif i == 2:
            counter.append('CASS ')
            score.append(result[0]['scores'])
        elif i == 3:
            counter.append('SAPPORO ')
            score.append(result[0]['scores'])
        elif i == 4:
            counter.append('TERRA ')
            score.append(result[0]['scores'])
        elif i == 5:
            counter.append('HEINEKEN ')
            score.append(result[0]['scores'])
        elif i == 6:
            counter.append('HITE_EXTRACOLD ')
            score.append(result[0]['scores'])
        elif i == 7:
            counter.append('HOEGAARDEN ')
            score.append(result[0]['scores'])
        elif i == 8:
            counter.append('KIRIN_ICHIBAN ')
            score.append(result[0]['scores'])
        elif i == 9:
            counter.append('KRONENBOURG ')
            score.append(result[0]['scores'])
        elif i == 10:
            counter.append('ASAHI ')
            score.append(result[0]['scores'])
        
    image_info_counter.append(collections.Counter(counter))
    image_info_score.append(score)
    
    len(image_info_counter)
    len(image_info_score)

df = DataFrame({'name':image_info_name, 'result':image_info_score,'count':image_info_counter}) # 변수리스트에서 표형식의 데이터프레임 드래그해서 결과값 추출



# 이미지 정보 리스트 텍스트 파일로 만들기3 (정확도 평균)
import skimage.io
import sys
import pandas as pd
import collections
from pandas import DataFrame
sys.path.append('C:/data/Mask_RCNN/samples/Logo/Utility') # 유틸리티 경로 추가

import imageUtil
imagename_list = imageUtil.image_path('C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/val') # 이미지가 있는 폴더 경로 설정

BUDWEISSER = []
CASS = []
SAPPORO = []
TERRA = []
HEINEKEN = []
HITE_EXTRACOLD = []
HOEGAARDEN = []
KIRIN_ICHIBAN = []
KRONENBOURG = []
ASAHI = []
logo_score_list = [BUDWEISSER, CASS, SAPPORO, TERRA, HEINEKEN, HITE_EXTRACOLD, HOEGAARDEN, KIRIN_ICHIBAN, KRONENBOURG, ASAHI]

x = 0
list_num = 0
for i in range(10):
    
    for j in range(20):
        image = skimage.io.imread(imagename_list[x])
        
        result = model.detect([image], verbose=1) # 객체 탐지 
        
#        image_info_list.append(str(str(e.split('/')[-1]) + '  ' + str(result[0]['class_ids'])+ '  ' + str(result[0]['scores']) + '\n'))
        
        for k in result[0]['scores']:
            logo_score_list[list_num].append(k)
        
        x += 1
    list_num += 1

logo_avg = []
for i in logo_score_list:
    logo_avg.append(sum(i) / len(i))

# 순서대로 실행하면 안됌, 
logo_avg_6000 = logo_avg # 가중치 6000번 돌린 모델로 설정하고 위 for 문 돌리고 실행
len(logo_avg_6000)


logo_avg_20000 = logo_avg # 가중치 20000번 돌린 모델로 설정하고 위 for 문 돌리고 바로위 logo_avg_6000 = logo_avg 실행하지말고 실행
len(logo_avg_20000)


df = DataFrame({'6000':logo_avg_6000, '20000':logo_avg_20000}) # 변수리스트에서 표형식의 데이터프레임 드래그해서 결과값 추출



# 탐지된 이미지 리스트 폴더에 이미지로 저장하기 (미완)
from PIL import Image
os.chdir("C:/data/Mask_RCNN/samples/Logo/detected_image") # 저장하는 폴더 위치 설정

#plt.figure(figsize=(13,13)) # 탐지된 이미지 확인
#plt.imshow(detected_image) # 탐지된 이미지 확인

import skimage.io
import sys
import pandas as pd
sys.path.append('C:/data/Mask_RCNN/samples/Logo/Utility') # 유틸리티 경로 추가

import imageUtil
imagename_list = imageUtil.image_path('C:/data/Mask_RCNN (colab)/samples/Logo/logo_dataset_/val') # 이미지가 있는 폴더 경로 설정

x = 1
for e in imagename_list:
    image = skimage.io.imread(e)
    
    # Run object detection
    result = model.detect([image], verbose=1) # 객체 탐지 
    
    ax = visualize.display_instances(image, 
                                     result[0]['rois'], 
                                     result[0]['masks'], 
                                     result[0]['class_ids'], 
                                     dataset.class_names, 
                                     result[0]['scores'], 
                                     ax=ax,
                                     title="Logo Predictions")
    
    print("result[0]['class_ids'] : " + str(result[0]['class_ids'])) # [5, 5]
    
    print("ax : " + ax)
    
    img = Image.fromarray(detected_image, 'RGB') # 배열로 나온 이미지 정보를 이미지로 변환

    img.save(e.split('/')[-1]) # 이미지로 설정한 폴더에 이미지 이름 그대로 저장
    
    x += 1
    
    if x == 3:
        break

