import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import cv2

def select_polygon(image):
    #image = cv2.imread(imagePath)
    plt.imshow(image)
    print("Please click")
    x = plt.ginput(-1)
    print("clicked", x)
    # plt.show()
    #matplotlib.pyplot.ginput(n=1, timeout=30, show_clicks=True, mouse_add=1, mouse_pop=3, mouse_stop=2)
    print(x)
    return x

def create_mask(image, polygon = False):
    if polygon == False:
        polygon = select_polygon(image)
    height,width,depth = image.shape
    imageMask = Image.new('L', (width, height), 0)
    ImageDraw.Draw(imageMask).polygon(polygon, outline=1, fill=1)
    mask = np.array(imageMask)
    mask3d = np.dstack((mask,mask, mask))
    #print(mask)
    #plt.imshow(mask3d)
    #plt.waitforbuttonpress()
    print(image.shape)
    print(mask3d.shape)
    print(mask.shape)
    if depth == 3:
        print("returning 3 layer mask")
        return mask3d, depth
    elif depth == 1:
        print("returning 1 layer mask")
        return mask, depth
    else:
        print("ERROR - Image type not understood")
        return

def mask_off(mask, image):
    image1 = np.where(mask, image, np.nan)
    print(mask[50,50,:])
    print(image[50,50,:])
    print(image1[50,50,:])
    # image2 = np.where(mask, image[:,:,2], np.nan)
    # image0 = np.where(mask, image[:,:,0], np.nan)

    #Newimage = np.empty((height, width, 3))
    # Newimage[:,:,1] = image1
    # Newimage[:,:,2] = image2
    # Newimage[:,:,0] = image0
    #Newimage = np.dstack((image0,image1, image2))
    # current_cmap = plt.cm.get_cmap()
    # current_cmap.set_bad(color='red')
    # plt.imshow((image1).astype(np.uint8))
    # plt.waitforbuttonpress()
    return ((image1).astype(np.uint8))

def mask_off_average(mask, image):
    image3d = np.where(mask, image, np.nan)
    a0 = np.nanmean(image3d[:,:,0])
    a1 = np.nanmean(image3d[:,:,1])
    a2 = np.nanmean(image3d[:,:,2])
    image0 = np.where(mask[:,:,0], a0, np.nan)
    image1 = np.where(mask[:,:,0], a1, np.nan)
    image2 = np.where(mask[:,:,0], a2, np.nan)
    imageMaskAv = np.dstack((image0,image1, image2))
    # plt.imshow((imageMaskAv).astype(np.uint8))
    # plt.waitforbuttonpress()
    return ((imageMaskAv).astype(np.uint8))

def replace_masked_average(mask, image):
    image3d = np.where(mask, image, np.nan)
    a0 = np.nanmean(image3d[:,:,0])
    a1 = np.nanmean(image3d[:,:,1])
    a2 = np.nanmean(image3d[:,:,2])
    vector = [a0, a1, a2]
    image0 = np.where(mask[:,:,0], a0, image[:,:,0])
    image1 = np.where(mask[:,:,0], a1, image[:,:,1])
    image2 = np.where(mask[:,:,0], a2, image[:,:,2])
    imageMaskAv = np.dstack((image0,image1, image2))
    # plt.imshow((imageMaskAv))#.astype(np.uint8))
    # plt.waitforbuttonpress()
    return ((imageMaskAv)), vector      #.astype(np.uint8))

def main():
    image = cv2.imread('C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\0_depth.png')
    mask3d, depth = create_mask(image)
    print(depth)
    #maskedImage = mask_off(mask3d, image)
    # cv2.imshow("Masked Image", maskedImage)
    # cv2.waitKey(0)
    #masked = mask_off_average(mask3d, image)
    maskedArea = replace_masked_average(mask3d, image)
    cv2.imshow("Masked Image", maskedArea)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
