

import os
import re

# 디렉토리의 절대경로를 입력받아 해당 디렉토리의 이미지 파일의 경로을 출력
def image_path(image_file_absolute_path):
    return [image_file_absolute_path + '/' + file_name for file_name in os.listdir(image_file_absolute_path) if bool(re.search('(.png|.jpg)$', file_name))]

# 예제
if __name__== "__main__":
    import imageUtil
    
    image_path('/Users/yoonseojin/Logo_Recognition/data/YOLO MARK TEST')
    
