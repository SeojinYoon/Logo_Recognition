# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from imgaug import augmenters as iaa 
import numpy as np
import cv2 
import os

import imgaug as ia
import imgaug.augmenters as iaa

sometimes = lambda aug: iaa.Sometimes(0.5, aug)


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
        cv2.imwrite('%s/mo_%s_%d.jpg'%(name,number,i), images[i])
    print("image saving complete")
    

#여러 폴더에 한번에 저장하기  
def imagewriterfunction(folder, images):
    for i in range(0,len(images)):
        write_images(folder, str(i), images[i])
    print("all images saved to folder")    


#이미지 증강 코드
def augmentations1(images):
    seq1 = iaa.Sequential([
#            iaa.Canny(alpha=0.5),
            iaa.Rot90(k=2),
            iaa.Snowflakes(density=(0.02,0.17))
#            iaa.MotionBlur(k=5)
#            iaa.Superpixels(n_segments=150, p_replace=0.1)            
#            iaa.AverageBlur(k=(2,7)),
#            iaa.Crop(px=(1, 16), keep_size=False),
#            iaa.Fog()
    ])

    seq2 = iaa.Sequential([
            iaa.Grayscale(alpha=1),
            iaa.CropToFixedSize(height=200,width=200,position="left-center")
#            iaa.ChannelShuffle(p=1.0),
#            iaa.PerspectiveTransform(scale=(0.01, 0.1))])
    ])
    
    seq3 = iaa.Sequential([
            sometimes(iaa.CoarseDropout(p=0.1, size_percent=0.8, per_channel=True)),
            sometimes(iaa.Snowflakes(density=(0.005,0.075))),
            sometimes(iaa.Rot90(k=1)),
            sometimes(iaa.Affine(
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)}, # scale images to 80-120% of their size, individually per axis
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}, # translate by -20 to +20 percent (per axis)
            rotate=(-45, 45), # rotate by -45 to +45 degrees
            shear=(-16, 16), # shear by -16 to +16 degrees
            order=[0, 1], # use nearest neighbour or bilinear interpolation (fast)
            cval=(0, 255), # if mode is constant, use a cval between 0 and 255
            mode=ia.ALL)) # use any of scikit-image's warping modes (see 2nd image from the top for examples)
    ])
            
    seq4 = iaa.Sequential([
            iaa.AddToHue((-45,45)),
            iaa.CropAndPad(
                    percent=(-0.25, 0.25),
                    pad_mode=ia.ALL,
                    pad_cval=(0, 255)),
            iaa.SigmoidContrast(per_channel=True),
            iaa.GammaContrast(per_channel=True),
            sometimes(iaa.Invert(per_channel=True))
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




photos = 'c:\\Users\\stu19\\Desktop\\project_brandlogo\\data\\__BRAND LOGO__' #이미지 읽어올 경로
folder = os.listdir(photos)


photos1 = load_images_from_folder(os.path.join(photos, folder[0]))
photos2 = load_images_from_folder(os.path.join(photos, folder[1]))
photos3 = load_images_from_folder(os.path.join(photos, folder[2]))
photos4 = load_images_from_folder(os.path.join(photos, folder[3]))
photos5 = load_images_from_folder(os.path.join(photos, folder[4]))
photos6 = load_images_from_folder(os.path.join(photos, folder[5]))
photos7 = load_images_from_folder(os.path.join(photos, folder[6]))
photos8 = load_images_from_folder(os.path.join(photos, folder[7]))
photos9 = load_images_from_folder(os.path.join(photos, folder[8]))
photos10 = load_images_from_folder(os.path.join(photos, folder[9]))
photos11 = load_images_from_folder(os.path.join(photos, folder[10]))
photos12 = load_images_from_folder(os.path.join(photos, folder[11]))
photos13 = load_images_from_folder(os.path.join(photos, folder[12]))
photos14 = load_images_from_folder(os.path.join(photos, folder[13]))
photos15 = load_images_from_folder(os.path.join(photos, folder[14]))
photos16 = load_images_from_folder(os.path.join(photos, folder[15]))


photo_augmented1234 = augmentations1(photos1) #이미지 증강 0,1,2,3 이 리스트 형태로 있다
photo_augmented1234 = augmentations1(photos2)
photo_augmented1234 = augmentations1(photos3)
photo_augmented1234 = augmentations1(photos4)
photo_augmented1234 = augmentations1(photos5)
photo_augmented1234 = augmentations1(photos6)
photo_augmented1234 = augmentations1(photos7)
photo_augmented1234 = augmentations1(photos8)
photo_augmented1234 = augmentations1(photos9)
photo_augmented1234 = augmentations1(photos10)
photo_augmented1234 = augmentations1(photos11)
photo_augmented1234 = augmentations1(photos12)
photo_augmented1234 = augmentations1(photos13)
photo_augmented1234 = augmentations1(photos14)
photo_augmented1234 = augmentations1(photos15)
photo_augmented1234 = augmentations1(photos16)


write_images('c:/data/aug/asahi0', 'Tsingtao', photo_augmented1234[0]) 
write_images('c:/data/aug/asahi1', 'CASS_Fresh', photo_augmented1234[1]) 
write_images('c:/data/aug/asahi2', 'CASS_Fresh', photo_augmented1234[2]) 
write_images('c:/data/aug/asahi3', 'CASS_Fresh', photo_augmented1234[3])
