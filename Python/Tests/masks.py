import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import cv2

def create_mask(image):
    plt.imshow(image)
    print("Please click")
    x = plt.ginput(-1)
    print("clicked", x)
    # plt.show()
    #matplotlib.pyplot.ginput(n=1, timeout=30, show_clicks=True, mouse_add=1, mouse_pop=3, mouse_stop=2)
    polygon = x
    height,width,depth = image.shape
    imageMask = Image.new('L', (width, height), 0)
    ImageDraw.Draw(imageMask).polygon(polygon, outline=1, fill=1)
    mask = np.array(imageMask)
    mask3d = np.dstack((mask,mask, mask))
    #print(mask)
    plt.imshow(mask)
    plt.waitforbuttonpress()
    return mask3d
    

def use_mask(image, mask3d):
    #print(image.shape)
    #print(mask3d.shape)
    #print(mask.shape)
    image1 = np.where(mask3d, image, np.nan)
    print(mask3d[50,50,:])
    print(image[50,50,:])
    print(image1[50,50,:])
    # image2 = np.where(mask, image[:,:,2], np.nan)
    # image0 = np.where(mask, image[:,:,0], np.nan)
    #Newimage = np.empty((height, width, 3))
    # Newimage[:,:,1] = image1
    # Newimage[:,:,2] = image2
    # Newimage[:,:,0] = image0
    #Newimage = np.dstack((image0,image1, image2))
    #current_cmap = plt.cm.get_cmap()
    #current_cmap.set_bad(color='red')
    #plt.imshow((image1).astype(np.uint8))
    #plt.waitforbuttonpress()
    return ((image1).astype(np.uint8))

def main():
    image = plt.imread("C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\0_depth.png")
    mask3d = create_mask(image)
    plt.imshow(mask3d)
    plt.waitforbuttonpress()
    maskedImage = use_mask(image, mask3d)
    print("displaynig figure")
    plt.imshow(maskedImage)
    plt.waitforbuttonpress()

if __name__ == "__main__":
    main()
