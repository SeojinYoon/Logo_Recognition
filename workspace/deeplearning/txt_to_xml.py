from lxml import etree
from PIL import Image
import csv
import os

# 이미지 경로 
IMG_PATH = "C:/mark_transformer/img"
fw = os.listdir(IMG_PATH) #이미지 경로에 있는 파일 출력

# 새로 생성될 xml파일을 저장할 경로(new_가 새로운 파일 이름 앞에 붙어서 나옴)
# path of save xml file 
save_path = 'C:/mark_transformer/new/new_'

# 변환해야 할 txt파일이 들어있는 경로(다크넷 rectbox 했던 것) 
# txt_folder is txt file root that using darknet rectbox
txt_folder = 'C:/mark_transformer/old'
 
# label 이름
# edit ypur label set
labels = [0,1,2,3,4,5,6,7,8,9]

# txt파일을 읽기 위한 함수 
def csvread(fn):
    with open(fn, 'r') as csvfile:
        list_arr = []
        reader = csv.reader(csvfile, delimiter=' ')
 
        for row in reader:
            list_arr.append(row)
    return list_arr

'''
csvread('C:/mark_transform_test/mark/google_hoegaarden4.txt') 

Out[210]: 
[['7', '0.260156', '0.638889', '0.293750', '0.122222'],
 ['7', '0.669531', '0.509722', '0.382813', '0.094444']]
'''

# 뭔지 모르겠지만 여기서 global변수 관련 에러가 나서 수정함 
'''
def convert_label(txt_file):
    if((txt_file[0]) == str(0)):
        global label
        label = 'beer'
 
    return label
'''
object_id = {'0' : 'ASAHI',
             '1' : 'BUDWEISSER',
             '2' : 'CASS',
             '3' : 'SAPPORO',
             '4' : 'TERRA',
             '5' : 'HEINEKEN',
             '6' : 'HITE_EXTRACOLD',
             '7' : 'HOEGAARDEN',
             '8' : 'KIRIN_ICHIBAN',
             '9' : 'KRONENBOURG'}


def convert_label(txt_file):
    for i in txt_file:
        if i[0] in object_id.keys():
            return object_id[i[0]]

# txt 파일의 값들을 xml파일의 값들처럼 변환하는 함수
# core code = convert the yolo txt file to the x_min,x_max...
def extract_coor(txt_file, img_width, img_height):
    x_rect_mid = float(txt_file[1])
    y_rect_mid = float(txt_file[2])
    width_rect = float(txt_file[3])
    height_rect = float(txt_file[4])
 
    x_min_rect = ((2 * x_rect_mid * img_width) - (width_rect * img_width)) / 2
    x_max_rect = ((2 * x_rect_mid * img_width) + (width_rect * img_width)) / 2
    y_min_rect = ((2 * y_rect_mid * img_height) -
                  (height_rect * img_height)) / 2
    y_max_rect = ((2 * y_rect_mid * img_height) +
                  (height_rect * img_height)) / 2
 
    return x_min_rect, x_max_rect, y_min_rect, y_max_rect
 
 
for line in fw:
    root = etree.Element("annotation")
 
    # try debug to check your path
    img_style = IMG_PATH.split('/')[-1]
    img_name = line
    image_info = IMG_PATH + "/" + line
    img_txt_root = txt_folder + "/" + line[:-4]
    txt = ".txt"
 
    txt_path = img_txt_root + txt
    txt_file = csvread(txt_path)
    ######################################
 
    # read the image  information
    img_size = Image.open(image_info).size
 
    img_width = img_size[0]
    img_height = img_size[1]
    img_depth = Image.open(image_info).layers
    ######################################
 
    folder = etree.Element("folder")
    folder.text = "%s" % (img_style)
 
    filename = etree.Element("filename")
    filename.text = "%s" % (img_name)
 
    path = etree.Element("path")
    path.text = "%s" % (IMG_PATH)
 
    source = etree.Element("source")
    ##################source - element##################
    source_database = etree.SubElement(source, "database")
    source_database.text = "Unknown"
    ####################################################
 
    size = etree.Element("size")
    ####################size - element##################
    image_width = etree.SubElement(size, "width")
    image_width.text = "%d" % (img_width)
 
    image_height = etree.SubElement(size, "height")
    image_height.text = "%d" % (img_height)
 
    image_depth = etree.SubElement(size, "depth")
    image_depth.text = "%d" % (img_depth)
    ####################################################
 
    segmented = etree.Element("segmented")
    segmented.text = "0"
 
    root.append(folder)
    root.append(filename)
    root.append(path)
    root.append(source)
    root.append(size)
    root.append(segmented)
 
    for ii in range(len(txt_file)):
 
        label = convert_label(txt_file[ii][0])
        x_min_rect, x_max_rect, y_min_rect, y_max_rect = extract_coor(
            txt_file[ii], img_width, img_height)
 
        object = etree.Element("object")
        ####################object - element##################
        name = etree.SubElement(object, "name")
        name.text = "%s" % (label)
 
        pose = etree.SubElement(object, "pose")
        pose.text = "Unspecified"
 
        truncated = etree.SubElement(object, "truncated")
        truncated.text = "0"
 
        difficult = etree.SubElement(object, "difficult")
        difficult.text = "0"
 
        bndbox = etree.SubElement(object, "bndbox")
        #####sub_sub########
        xmin = etree.SubElement(bndbox, "xmin")
        xmin.text = "%d" % (x_min_rect)
        ymin = etree.SubElement(bndbox, "ymin")
        ymin.text = "%d" % (y_min_rect)
        xmax = etree.SubElement(bndbox, "xmax")
        xmax.text = "%d" % (x_max_rect)
        ymax = etree.SubElement(bndbox, "ymax")
        ymax.text = "%d" % (y_max_rect)
        #####sub_sub########
 
        root.append(object)
        ####################################################
 
    file_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
    print(file_output.decode('utf-8'))
    ff = open('%s%s.xml' % (save_path, img_name[:-4]), 'w', encoding="utf-8")
    ff.write(file_output.decode('utf-8'))
    ff.close()
    