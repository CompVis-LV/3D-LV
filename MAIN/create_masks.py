import cv2
import os
import createMask as cm




def main():
    os.chdir(r"C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\tPrism")
    for x in range(8):
        colourImagePath = "%s_colour.png" % (x)
        #colourImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\hexagon.png"
        #depthImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\hexagon.png"
        image = cv2.imread(colourImagePath)
        #CREATE MASK
        mask = image.copy()
        layers = 0
        mask, layers = cm.create_mask(image)
        cv2.imwrite( "%s_mask.png" % (x), (mask*255).astype(np.uint8))
        maskedImage = cm.mask_off(mask, image)
        cv2.imwrite( "%s_maskedImage.png" % (x), (maskedImage).astype(np.uint8))
        maskedDepthImage = cm.mask_off(mask, depthImage)

if __name__ == "__main__":
    main()
