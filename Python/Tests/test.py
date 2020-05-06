import argparse
import imutils
import cv2
import os

image = cv2.imread('C:/Users/Jared/Documents/ECTE458//3D-LV//test//front.jpg')


resized = imutils.resize(image, width=900)
cv2.imshow("resized", resized)
cv2.waitKey(0)