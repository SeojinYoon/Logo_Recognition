# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from imgaug import augmenters as iaa 
import numpy as np
import cv2 
import os



#이미지 읽어오는 함수
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images
   

#이미지 저장 함수
def write_images(name,number,images):
    for i in range(0,len(images)):
        cv2.imwrite('%s/mo_%s_%d.jpg'%(name,number,i), images[i]) #이미지 저장할 경로 설정을 여기서 한다.
    print("image saving complete")
    

#여러 폴더에 한번에 저장하기  
def imagewriterfunction(folder, images):
    for i in range(0,len(images)):
        write_images(folder, str(i), images[i])
    print("all images saved to folder")    


#이미지 증강 코드
def augmentations1(images):
    seq1 = iaa.Sequential([
        iaa.AverageBlur(k=(2,7)),
        iaa.Crop(px=(1, 16), keep_size=False)
    ])

    seq2 = iaa.ChannelShuffle(p=1.0)
    seq3 = iaa.CoarseDropout(p=(0.1, 0.3))
    seq4 = iaa.Sequential([
        iaa.Add((-15,15)),
        iaa.Multiply((0.3, 1.5))
    ])
    print("image augmentation beginning")
    img1=seq1.augment_images(images)
    print("sequence 1 completed......")
    img2=seq2.augment_images(images)
    print("sequence 2 completed......")
    img3=seq3.augment_images(images)
    print("sequence 3 completed......")
    img4=seq4.augment_images(images)
    print("sequence 4 completed......")
    print("proceed to next augmentations")
    list = [img1, img2, img3, img4]
    return list



photos = 'c:\\Users\\stu19\\Desktop\\project_brandlogo\\data' #이미지 읽어올 경로
folder = os.listdir(photos)


photos1 = load_images_from_folder(os.path.join(photos, folder[0]))
photos2 = load_images_from_folder(os.path.join(photos, folder[1]))
photos3 = load_images_from_folder(os.path.join(photos, folder[2]))





photo_augmented1234 = augmentations1(photos1) #이미지 증강 0,1,2,3 이 리스트 형태로 있다

write_images('c:/data/aug', 'ASAHI', photo_augmented1234[0]) 


