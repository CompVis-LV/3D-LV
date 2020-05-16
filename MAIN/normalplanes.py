import sys
sys.path.append('C:\\Users\\Jared\\Documents\ECTE458\\3D-LV\Python\\Tests')
import numpy as np
import argparse
import cv2
import signal
from createMask import create_mask
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
            print(itm)
            
            return normals, shape, itm

def remove_common_noise(normals, shape, itm):
    for i in range(1,shape[1]-1):
        for j in range(1,shape[0]-1):
            if ("%s%s%s" % (normals[j,i,0], normals[j,i,1], normals[j,i,2])) == itm:
                normals[j,i,:] = np.nan
                #print("nannafide")
    return normals

# normals = normals[1:h-1, 1:w-1, :]
# h,w,d = normals.shape
# print("%s%s%s" % (h, w, d))

def main():
    imagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\0_depth.png"
    image = cv2.imread(imagePath)
    shape = np.empty([1,3])
    #normals = image.copy()
    print("extracting normals")
    (normals, shape, itm) = extract_normals(image)
    cv2.imshow("normals", normals)
    cv2.waitKey(0)
    print(itm)
    print("Normals extracted, removing noise")
    normals = remove_common_noise(normals, shape, itm)
    #save image to be passed and openned as plt
    #create correct masking
    #cv2.imwrite('temp.png', normals) 
    print("Noise removed, create a mask")
    # fromCenter = False
    # mask3d = create_mask(normals)
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