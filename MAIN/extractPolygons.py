import numpy as np
import argparse
import cv2
import createMask as cm

def face_amount(image):
    cv2.imshow("Start Image", image)
    cv2.waitKey(0)
    value = input("Please enter an integer:\n")
    return int(value)

def extract_polygons(image, number):
    listoflists = []
    for count in range(number):
        poly = cm.select_polygon(image)
        listoflists.append(poly)
    return listoflists

def main():
    imagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\test7\\2_colour.png"
    image = cv2.imread(imagePath)
    #Select number of faces
    value = face_amount(image)
    #Extract polygons
    polygons = extract_polygons(image, value)


if __name__ == "__main__":
    main()
