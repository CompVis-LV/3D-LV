import numpy as np
import argparse
import cv2
from PIL import Image
from matplotlib import cm
import os

def fill_holes(depthImage):
    h,w,d = depthImage.shape
    mask = np.empty([h, w], np.int8)
    for i in range(1,h-1):
        for j in range(1,w-1):
            #print("%s%s%s" % (depthImage[i,j,0], depthImage[i,j,1], depthImage[i,j,2]))
            if ("%s%s%s" % (depthImage[i,j,0], depthImage[i,j,1], depthImage[i,j,2])) == str('000'):
                mask[i, j] = np.int8(1)
                #print("400!!!!!")
            else:
                mask[i, j] = np.int8(0)
                #print('0 was saved yo')
    cv2.imwrite("temp.bmp", mask)
    mask2 = cv2.imread("temp.bmp", cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("bfshbf", mask2)
    # cv2.waitKey(0)
    os.remove("temp.bmp")
    print("File Removed!")
    #print(mask[1, 2].bit_length())
    return cv2.inpaint(depthImage, mask2, 3, cv2.INPAINT_TELEA)



def main():
    depthImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\test7\\2_depth.png"
    #fill depth holes
    depthImage = cv2.imread(depthImagePath)
    image = fill_holes(depthImage)
    cv2.imshow("bfshbf", image)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()

