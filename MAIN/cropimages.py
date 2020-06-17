import cv2
import os
import createMask as cm
import numpy as np
import fillHoles as fh

def main():
    os.chdir(r"C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Images")
    img = cv2.imread("3.png")
    crop_img = img[110:355, 240:600]
    cv2.imwrite("3c.png", crop_img)
    cv2.waitKey(0)

    # mask = cv2.imread('8_mask.png')
    # mask = mask/255
    # depthImage = cv2.imread('8_depth.png')
    # #depthImage = fh.fill_holes(depthImage)
    # maskedDepthImage = cm.mask_off(mask, depthImage)
    # cv2.imshow( "8_maskedDepthImage.png", maskedDepthImage)
    # cv2.waitKey(0)
    # cv2.imwrite( "8_maskedDepthImage.png", (maskedDepthImage).astype(np.uint8))


if __name__ == "__main__":
    main()