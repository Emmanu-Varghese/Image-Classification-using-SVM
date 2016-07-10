import cv2
import numpy
import numpy as np
import Image
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


path1='d:\\Emmanu\\project-data\\training-set\\1\\'
path2='d:\\Emmanu\\project-data\\training-set\\2\\'
path3='d:\\Emmanu\\project-data\\training-set\\3\\'
training_set = []
training_labels=[]

training_set1 = []
training_labels1=[]
listing1 = os.listdir(path1)
listing2=os.listdir(path2)
listing3=os.listdir(path3)


for file in listing1:
    img = cv2.imread(path1 + file)
    h=hog(img)
    training_set.append(h)
    training_labels.append(1)
for file in listing2:
    img = cv2.imread(path2 + file)
    h=hog(img)
    training_set.append(h)
    training_labels.append(2)
for file in listing3:
    img = cv2.imread(path3 + file)
    h=hog(img)
    training_set.append(h)
    training_labels.append(2)


######     SVM training     ########################


trainData=np.float32(training_set)
responses=np.float32(training_labels)
svm = cv2.SVM()
svm.train(trainData,responses, params=svm_params)
svm.save('hog_svm_data1.dat')

for file in listing2:
    img = cv2.imread(path2 + file)
    h=hog(img)
    training_set1.append(h)
    training_labels1.append(2)
for file in listing3:
    img = cv2.imread(path3 + file)
    h=hog(img)
    training_set1.append(h)
    training_labels1.append(3)
trainData=np.float32(training_set1)
responses=np.float32(training_labels1)
svm1 = cv2.SVM()
svm1.train(trainData,responses, params=svm_params)
svm1.save('hog_svm_data2.dat')




