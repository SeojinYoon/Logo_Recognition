# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:01:44 2019

@author: sty13
"""

# * 텐서플로우하고 케라스가 이미 설치되어 있으면 skip
# 아나콘다 프롬프트를 관리자 권한으로 실행 후 아래 명령어를 실행하여 설치
# conda install tensorflow==1.14.0
# conda install keras

import os
os.chdir('C:/data/Mask_RCNN')

pip install -r requirements.txt

os.chdir('C:/data/Mask_RCNN/samples')

import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

# 프로젝트의 루트 디렉토리
ROOT_DIR = os.path.abspath("../")

import warnings
warnings.filterwarnings("ignore")



# 임포트 mask RCNN
sys.path.append(ROOT_DIR) # 라이브러리의 로컬 버전을 찾으려면
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

# COCO 설정 가져 오기
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/")) # 로컬 버전을 찾으려면

# 패키지를 설치하라고 에러가 나서 아나콘다 프롬프트로 conda install -c conda-forge 명령어 실행
# opencv 관련 패키지 에러나서 개인적으로 opencv-python 설치를 위해  pip install opencv-python 명령어 실행
# pip install opencv-python
import imgaug

# 패키지를 설치하라고 에러가 나서 아나콘다 프롬프트로 conda install git 명령어 실행
#pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
import pycocotools
import coco

%matplotlib inline



# 로그 및 훈련 된 모델을 저장하는 디렉토리
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# 훈련 된 웨이트 파일의 로컬 경로
COCO_MODEL_PATH = os.path.join('', "mask_rcnn_test.h5")

# 필요한 경우 릴리스에서 COCO 훈련 가중치를 다운로드하십시오
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

# 탐지를 실행할 이미지 디렉토리
IMAGE_DIR = os.path.join(ROOT_DIR, "images")



class InferenceConfig(coco.CocoConfig):
    # 추론을 실행하기 때문에 배치 크기를 1로 설정하십시오.
    # 한 번에 하나의 이미지. 배치 크기 = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()



# 추상화 모드에서 모델 객체를 만듭니다.
model = modellib.MaskRCNN(mode="inference", model_dir='mask_rcnn_balloon.hy', config=config)

# MS-COCO 으로 학습된 가중치 로드
model.load_weights('mask_rcnn_coco.h5', by_name=True)



# COCO 클래스 이름
class_names = ['BG', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']



## * 원래 방법
## 이미지 폴더에서 임의의 이미지를로드
#image = skimage.io.imread('sample5.jpg')
#
## 원본 이미지
#plt.figure(figsize=(12,10))
#skimage.io.imshow(image)

# * 내가 수정한 방법 ( (1024,1024,3) 처럼 RGB 모양이 되야하는데 내 컴퓨터에서는 (1024,1024,4) 이런식으로 sRGB? 으로 표시되기에 Image 클래스를 사용하여 RGB 로 convert 하였음 ) 
# 이미지 폴더에서 임의의 이미지를로드
os.chdir('C:/data/Mask_RCNN/samples')
image = Image.open('sample6.png')

# 원본 이미지
plt.figure(figsize=(12,10))
plt.imshow(image)

image = image.convert("RGB")
image = np.array(image)
image.shape

# 감지 시작
results = model.detect([image], verbose=1)

# 결과 시각화
r = results[0]
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])



# 모델에서 예측한 모든 마스크를 가져와서 마스크 변수에 저장
mask = r['masks'] # bool 형식
mask = mask.astype(int) # 숫자 형식 (0 과 1) 로 변환
mask.shape # (height, width, class count) 여기서 3번째 열은 모델에 의해 검출된 객체 수이다.
# 여기서 0 은 특정 픽셀에 객체가 없음을 의미하고 1 은 해당 픽셀에 객체가 있음을 의미한다. 마스크의 모양은 원본 이미지의 모양과 비슷함.



# 각 세그먼트 출력, 각 마스크에 원본 이미지를 곱해서 세그먼트 각 세그먼트 가져온다.
for i in range(mask.shape[2]): # 검출된 객체수
    temp = skimage.io.imread('sample1.png') # temp = image 로 설정하면 처음 이미지만 출력되고 나머지 이미지는 출력 안됨
    for j in range(temp.shape[2]): # RGB 인듯
        temp[:,:,j] = temp[:,:,j] * mask[:,:,i]
    plt.figure(figsize=(8,8))
    plt.imshow(temp)





# 위에 있는 소스코드가 mask_r_cnn_2.0.py 처럼 실행되지 않아서 아래와 같은 주피터에서 실행되는 소스코드를 가져와 실행했음
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
#ROOT_DIR = os.path.abspath("./") # 따로 이것만 실행
ROOT_DIR = "C:/data/Mask_RCNN" # 따로 이것만 실행

os.chdir('C:/data/Mask_RCNN') # mrcnn 를 import 하기위한 workspace path 설정

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
MODEL_DIR = os.path.join(ROOT_DIR, "samples\\mask_rcnn_test.h5") # 가중치를 사용하는 모델 실제 경로

# Path to Ballon trained weights
# You can download this file from the Releases page
# https://github.com/matterport/Mask_RCNN/releases
BALLON_WEIGHTS_PATH = os.path.join(ROOT_DIR, "samples\\mask_rcnn_coco.h5")  # 가중치 경로

print(ROOT_DIR)
print(MODEL_DIR)
print(BALLON_WEIGHTS_PATH)

# * Configurations
config = balloon.BalloonConfig()
BALLOON_DIR = os.path.join(ROOT_DIR, "samples\\balloon\\test_dataset")

print(BALLOON_DIR)

# Override the training configurations with a few
# changes for inferencing.
class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

# * Notebook Preferences
# Device to load the neural network on.
# Useful if you're training a model on the same 
# machine, in which case use CPU and leave the
# GPU for training.
DEVICE = "/cpu:0"  # /cpu:0 or /gpu:0

# Inspect the model in training or inference modes
# values: 'inference' or 'training'
# TODO: code for 'training' test mode not ready yet
TEST_MODE = "inference"

def get_ax(rows=1, cols=1, size=16):
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.
    
    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

# * Load Validation Dataset
# Load validation dataset
dataset = balloon.BalloonDataset()
dataset.load_balloon(BALLOON_DIR, "val")

# Must call before using the dataset
dataset.prepare()

print("Images: {}\nClasses: {}".format(len(dataset.image_ids), dataset.class_names))

print(BALLOON_DIR)

# * Load Model
# Create model in inference mode
with tf.device(DEVICE):
    model = modellib.MaskRCNN(mode="inference", 
                              model_dir=MODEL_DIR,
                              config=config)

print(MODEL_DIR)

# Set path to balloon weights file

# Download file from the Releases page and set its path
# https://github.com/matterport/Mask_RCNN/releases
# weights_path = "/path/to/mask_rcnn_balloon.h5"

# Or, load the last model you trained
weights_path = MODEL_DIR

# Load weights
print("Loading weights ", weights_path)
model.load_weights(weights_path, by_name=True)

print(weights_path)

dataset.class_from_source_map
dataset.class_info



# * Run Detection
image_id = random.choice(dataset.image_ids)
image, image_meta, gt_class_id, gt_bbox, gt_mask =\
    modellib.load_image_gt(dataset, config, image_id, use_mini_mask=False)
info = dataset.image_info[image_id]
print("image ID: {} 다음 {} 다음 ({}) 다음 {}".format(info["source"],
                                       info["id"],
                                       image_id, 
                                       dataset.image_reference(image_id)))

# Run object detection
results = model.detect([image], verbose=1)

# Display results
ax = get_ax(1)
r = results[0]
visualize.display_instances(image, 
                            r['rois'], 
                            r['masks'], 
                            r['class_ids'], 
                            dataset.class_names, 
                            r['scores'], 
                            ax=ax,
                            title="Predictions")
log("gt_class_id", gt_class_id)
log("gt_bbox", gt_bbox)
log("gt_mask", gt_mask)

# * Color Splash
splash = balloon.color_splash(image, r['masks'])
display_images([splash], cols=1)

