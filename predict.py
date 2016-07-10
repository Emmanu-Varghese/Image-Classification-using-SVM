import cv2
import numpy
from PIL import Image
import numpy as np

import os
from matplotlib import pyplot as plt
bin_n = 16 # Number of bins
def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n*ang/(2*np.pi))    # quantizing binvalues in (0...16)
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)     # hist is a 64 bit vector
    return hist
print "OpenCV version :  {0}".format(cv2.__version__)
svm_params = dict( kernel_type = cv2.SVM_LINEAR,
                    svm_type = cv2.SVM_C_SVC,
                    C=2.67, gamma=5.383 )

def predict_class(path):
    pre_out=''
    print type(pre_out)
    training_set = []
    test_set=[]
    color_test_set=[]
    training_labels=[]

    ######     SVM training     ########################

    svm = cv2.SVM()
    svm.load('hog_svm_data1.dat')

    ######     Now testing HOG     ########################

    img = cv2.imread(path)
    res=cv2.resize(img,(400,300))
    h=hog(res)
    test_set.append(h)
    testData = np.float32(test_set)
    result = svm.predict(testData)
    if result==1:
        pre_out+= 'Vehicle'
    elif result==2:
        pre_out+= 'Animal'
    elif result==3:
        pre_out+= 'Building'


    ######     Now testing Color      ########################

    svm1 = cv2.SVM()
    svm1.load('color_svm_data.dat')

    img = cv2.imread(path)
    res=cv2.resize(img,(400,300))
    crop_img = res[50:150, 100:200]
    cv2.imwrite("d:/Emmanu/project-data/color-test.jpg", crop_img)

    img = Image.open('d:/Emmanu/project-data/color-test.jpg')
    img200=img.convert('RGBA')
    arr= np.array(img200)
    flat_arr= arr.ravel()
    color_test_set.append(flat_arr)
    testData = np.float32(color_test_set)
    result = svm1.predict(testData)

    if result==1:
        pre_out+=' and '+ 'It has Red Shade'
    elif result==2:
        pre_out+=' and '+ 'It has Green Shade'
    elif result==3:
        pre_out+=' and '+ 'It has Blue Shade'
    elif result==4:
        pre_out+=' and '+ 'It has Black Shade'
    elif result==5:
        pre_out+=' and '+ 'It has Brown Shade'
    elif result==6:
        pre_out+=' and '+ 'It has Yellow Shade'
    elif result==7:
        pre_out+=' and '+ 'It has white Shade'
    return pre_out

def predict_shape(path,val):
    training_set = []
    test_set=[]
    test_set1=[]
    color_test_set=[]
    training_labels=[]
    result_list=[]

    ######     SVM training     ########################

    svm = cv2.SVM()
    svm.load('hog_svm_data1.dat')

    svm1 = cv2.SVM()
    svm1.load('hog_svm_data2.dat')

    ######     Now testing HOG     ########################

    img = cv2.imread(path)
    res=cv2.resize(img,(400,300))
    h=hog(res)
    test_set.append(h)
    testData = np.float32(test_set)
    pre_shape = svm.predict(testData)
    if val==3:
        if pre_shape==2:
            img = cv2.imread(path)
            res=cv2.resize(img,(400,300))
            h=hog(res)
            test_set1.append(h)
            testData = np.float32(test_set1)
            pre_shape = svm1.predict(testData)
            print 'inside'
            return pre_shape
    return pre_shape

def predict_color(path):

    training_set = []
    test_set=[]
    color_test_set=[]
    training_labels=[]
    result_list=[]
    ######     Now testing Color      ########################

    svm1 = cv2.SVM()
    svm1.load('color_svm_data.dat')

    img = cv2.imread(path)
    res=cv2.resize(img,(400,300))
    crop_img = res[50:150, 100:200]
    cv2.imwrite("d:/Emmanu/project-data/color-test.jpg", crop_img)

    img = Image.open('d:/Emmanu/project-data/color-test.jpg')
    img200=img.convert('RGBA')
    arr= np.array(img200)
    flat_arr= arr.ravel()
    color_test_set.append(flat_arr)
    testData = np.float32(color_test_set)
    pre_color = svm1.predict(testData)
    return pre_color

def main():
    print predict_shape('d:/Emmanu/project-data/tes.jpg')
if __name__ == '__main__':main()






