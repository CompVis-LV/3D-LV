import argparse
import imutils
import cv2
import os
import numpy as np

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
# image = cv2.imread('C:/Users/Jared/Documents/ECTE458//3D-LV//test//front.jpg')
# resized = imutils.resize(image, width=900)
# cv2.imshow("resized", resized)
# cv2.waitKey(0)
v1 = []
v2 = []
print(angle_between((0,1,0), (1, 0, 0)))