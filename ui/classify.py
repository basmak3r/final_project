#import required libraries 
#import OpenCV library
import cv2
#import matplotlib library
import matplotlib.pyplot as plt
#importing time library for speed comparisons of both classifiers
import time 
# %matplotlib inline


import argparse

parser = argparse.ArgumentParser(description='Image Inpainting')

parser.add_argument('--image1', type=str, default='../../dataset',
                    help='image dataset directory')

args = parser.parse_args()
# from utils.option import args

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#load test iamge

# print(args.image1)

test1 = cv2.imread(args.image1)

#convert the test image to gray image as opencv face detector expects gray images
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
#if you have matplotlib installed then 
plt.imshow(gray_img, cmap='gray')

# or display the gray image using OpenCV
# cv2.imshow('Test Imag', gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#load cascade classifier training file for haarcascade
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
#let's detect multiscale (some images may be closer to camera than others) images
faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
if len(faces)>0:
    print('True')
else:
    print('False')

#print the number of faces found
# print('Faces found: ', len(faces))