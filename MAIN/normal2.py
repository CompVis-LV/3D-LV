import sys
sys.path.append('C:\\Users\\Jared\\Documents\ECTE458\\3D-LV\Python\\Tests')
import numpy as np
import argparse
import cv2
import signal
import createMask as cm
import extractPolygons as ep
from functools import wraps
import errno
import os
import copy

def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm)

def extract_normals(d_im):
    print("extracting normals")
    d_im = d_im.astype("float64")
    normals = np.array(d_im, dtype="float32")
    h,w,d = d_im.shape
    shape = [h, w, d]
    print("%s%s%s" % (h, w, d))
    dict = {} 
    count, itm = 0, '' 
    for i in range(1,w-1):
        for j in range(1,h-1):
            t = np.array([i,j-1,d_im[j-1,i,0]],dtype="float64")
            f = np.array([i-1,j,d_im[j,i-1,0]],dtype="float64")
            c = np.array([i,j,d_im[j,i,0]] , dtype = "float64")
            d = np.cross(f-c,t-c)
            n = d / np.sqrt((np.sum(d**2)))
            normals[j,i,:] = n
            #print(n)
            item = ("%s%s%s" % (n[0], n[1], n[2]))
            #print(item)
            dict[item] = dict.get(item, 0) + 1
            if dict[item] >= count :
                count, itm = dict[item], item
    return normals, itm

def remove_noise_layer(normals, itm):
    h,w,d = normals.shape
    print("Normals extracted, removing noise")
    for i in range(1,w-1):
        for j in range(1,h-1):
            if ("%s%s%s" % (normals[j,i,0], normals[j,i,1], normals[j,i,2])) == itm:
                normals[j,i,:] = np.nan
                #print("nannafide")
    return normals


def main():
    imagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\3_Depth.png"
    d_im = cv2.imread(imagePath)
    shape = np.empty([1,3])
    normals, itm = extract_normals(d_im)
    print(itm)
    normals = remove_noise_layer(normals, itm)
    print("Noise removed, create a mask")
    cv2.imshow("Normals", normals)
    cv2.waitKey(0)
    number = ep.face_amount(normals)
##########################################################################################
# APPEND EACH POLYGON
    for count in range(number):
        r, depth = cm.create_mask(normals)
        imageMaskAv = cm.replace_masked_average(r, normals)
        cv2.imshow("Masked average", imageMaskAv)
        cv2.waitKey(0)
#########################################

    # r, depth = cm.create_mask(normals)
    # planeMask = cm.mask_off(r, normals)
    # a0 = np.nanmean(planeMask[:,:,0])
    # a1 = np.nanmean(planeMask[:,:,1])
    # a2 = np.nanmean(planeMask[:,:,2])
    # cv2.imshow("plane mask", planeMask)
    # cv2.waitKey(0)
    # print(planeMask[50,50,0])
    # print(planeMask[50,50,1])
    # print(planeMask[50,50,2])
    # print("a0 = %s, a1 = %s, a2 = %s" % (a0, a1, a2))
    # ## NAN AND VALUE NOT 0 and 1
    # image0 = np.where(planeMask[:,:,0], a0, np.nan) #(condition, true, false)
    # print(image0[50,50])
    # image1 = np.where(planeMask[:,:,1], a1, np.nan) #(condition, true, false)
    # print(image1[50,50])
    # image2 = np.where(planeMask[:,:,2], a2, np.nan) #(condition, true, false)
    # print(image2[50,50])
    # plane = np.dstack((image0,image1, image2))
    # print('plane dim')
    # print(plane.shape)
    # cv2.imshow("image 1", image0)
    # cv2.waitKey(0)
    # cv2.imshow("image 1", image1)
    # cv2.waitKey(0)
    # cv2.imshow("image 1", image2)
    # cv2.waitKey(0)
    # cv2.imshow("Plane", plane)
    # cv2.waitKey(0)
    # print(r[0], r[1], r[2], r[3])
    # print(a)
    # extract = normals[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
    # print(extract.shape)
    # cv2.imshow("extract", extract)
    # cv2.waitKey(0)

    # extract[:,:,1] = np.nanmean(extract)
    # extract[:,:,2] = np.nanmean(extract)
    # extract[:,:,0] = np.nanmean(extract)

    # cv2.imshow("extract", extract)
    # cv2.waitKey(0)


    # print(normals[0,0,:])

    # #cv2.imwrite("normal.jpg",normals*255)
    # cv2.imshow("normals", normals)
    # cv2.waitKey(0)

if __name__ == "__main__":
    main()