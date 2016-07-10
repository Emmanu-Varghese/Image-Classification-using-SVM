import cv2
from PIL import Image
import os
p = 5


def resize_all(path1,path2):
    global p
    resolution = (400,300)
    scaler = Image.ANTIALIAS
    if not os.path.exists(path2):
        os.makedirs(path2)
    listing=os.listdir(path1)
    for i,file_1 in enumerate(listing):
        img=Image.open(path1 + file_1)
        res=img.resize(resolution , Image.ANTIALIAS)
        res.save(path2+'p{}h{}.jpg'.format(p,i))
    p += 1


def main():

    global q
    path_list1=['d:\\Emmanu\\project-data\\vehicles\\Bikes\\','d:\\Emmanu\\project-data\\vehicles\\Cars\\','d:\\Emmanu\\project-data\\vehicles\\Bus\\','d:\\Emmanu\\project-data\\vehicles\\Trucks\\']
    path_list2=['d:\\Emmanu\\project-data\\Animals\\birds\\','d:\\Emmanu\\project-data\\Animals\\dogs\\','d:\\Emmanu\\project-data\\Animals\\lion\\','d:\\Emmanu\\project-data\\Animals\\squirrels\\','d:\\Emmanu\\project-data\\Animals\\tiger\\','d:\\Emmanu\\project-data\\Animals\\cow\\','d:\\Emmanu\\project-data\\Animals\\elephants\\','d:\\Emmanu\\project-data\\Animals\\giraffe\\','d:\\Emmanu\\project-data\\Animals\\bear\\','d:\\Emmanu\\project-data\\Animals\\crocodile\\']
    path_list3=['d:\\Emmanu\\project-data\\Humans\\faces\\']
    path_list4=['d:\\Emmanu\\project-data\\unclassified\\']
    path1='d:\\Emmanu\\project-data\\training-set\\1\\'
    path2='d:\\Emmanu\\project-data\\training-set\\2\\'
    path3='d:\\Emmanu\\project-data\\training-set\\3\\'
    path4='d:\\Emmanu\\project-data\\training-set\\4\\'
    for j in path_list1:
        resize_all(j, path1)
    print 'done'
    for j in path_list2:
        resize_all(j, path2)
    print 'done'
    for j in path_list3:
        resize_all(j, path3)
    print 'done'
    for j in path_list4:
        resize_all(j, path4)
    print 'done'

if __name__ == '__main__':main()
