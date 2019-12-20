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
ROOT_DIR = "C:\\data\\Mask_RCNN" # 가끔 선언이 안될 때가 있어서 따로 이것만 실행
os.chdir('C:\\data\\Mask_RCNN') # mrcnn 를 import 하기위한 workspace path 설정

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log
from samples.balloon import balloon

%matplotlib inline 


# Directory to save logs and trained model
MODEL_DIR = ROOT_DIR + "\\samples\\mask_rcnn_logo_test.h5" # 가중치를 사용하는 모델 실제 경로 (.h5 파일은 모델 아키텍처와 모델 가중치로 구성되어 있다)

# Path to Ballon trained weights
# You can download this file from the Releases page6
# https://github.com/matterport/Mask_RCNN/releases
weights_path = ROOT_DIR + "\\samples\\mask_rcnn_logo_test.h5"  # 가중치 경로 (.h5 파일은 모델 아키텍처와 모델 가중치로 구성되어 있다)
print(ROOT_DIR) # 경로확인
print(MODEL_DIR) # 경로확인
print(weights_path) # 경로확인

# * Configurations
config = balloon.BalloonConfig() # 환경설정 객체 생성
BALLOON_DIR = ROOT_DIR + "\\samples\\balloon\\test_dataset"
print(BALLOON_DIR)

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
DEVICE = "/cpu:0"  # /cpu:0 or /gpu:0

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
dataset = balloon.BalloonDataset() # 데이터셋 객체 생성
dataset.load_balloon(BALLOON_DIR, "val") # 검증 데이터셋 로드

# Must call before using the dataset
dataset.prepare()

print("Images: {}\n Classes: {}".format(len(dataset.image_ids), dataset.class_names))
print(BALLOON_DIR)


# * Load Model
# Create model in inference mode
with tf.device(DEVICE): # 모델 생성
    model = modellib.MaskRCNN(mode="inference", 
                              model_dir = MODEL_DIR,
                              config = config)
print(MODEL_DIR)

# Set path to balloon weights file

# Download file from the Releases page and set its path
# https://github.com/matterport/Mask_RCNN/releases
# weights_path = "/path/to/mask_rcnn_balloon.h5"

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
visualize.display_instances(image, 
                            r['rois'], 
                            r['masks'], 
                            r['class_ids'], 
                            dataset.class_names, 
                            r['scores'], 
                            ax=ax,
                            title="Logo Predictions")
log("gt_class_id", r['class_ids']) # 클래스 넘버 (0 부터 시작이기에 + 1 이 됨)
log("gt_bbox", r['rois']) # bounding box
log("gt_mask", r['masks']) # masking 영역


# * Color Splash
splash = balloon.color_splash(image, r['masks'])
display_images([splash], cols=1)




# * 원래 방법
# 이미지 폴더에서 임의의 이미지를로드
import skimage.io
os.chdir('C:/data/Mask_RCNN/samples')
image = skimage.io.imread('sample9.jpg')

plt.figure(figsize=(12,10))
skimage.io.imshow(image)

# * 내가 수정한 방법 ( (1024,1024,3) 처럼 RGB 모양이 되야하는데 내 컴퓨터에서는 (1024,1024,4) 이런식으로 sRGB? 으로 표시되기에 Image 클래스를 사용하여 RGB 로 convert 하였음 ) 
# 임의의 이미지 하나만 테스트해보고자 할 경우, RGB 가 4 일 경우 detection 을 위해 이미지를 3 으로 변환해야 할 경우
from PIL import Image
os.chdir('C:/data/Mask_RCNN/samples')

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


# 각 세그먼트 출력, 각 마스크에 원본 이미지를 곱해서 세그먼트 각 세그먼트 가져온다. (skimage.io.imread() 로 이미지를 로드했을 때만 사용가능)
for i in range(mask.shape[2]): # 검출된 객체수
    temp = skimage.io.imread('sample9.jpg') # temp = image 로 설정하면 처음 이미지만 출력되고 나머지 이미지는 출력 안됨
    for j in range(temp.shape[2]): # RGB 인듯
        temp[:,:,j] = temp[:,:,j] * mask[:,:,i]
    plt.figure(figsize=(8,8))
    plt.imshow(temp)


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

