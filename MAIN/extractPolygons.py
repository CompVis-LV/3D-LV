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

def extract_polygons_csv(file):
    lists =  np.loadtxt(open(file, "rb"), delimiter=",")
    polygons = []
    poly = []
    for rows in lists:
        print(rows)
        if str(rows[0]) != 'nan':
            poly.extend([(rows[2], rows[3])])
        else:
            polygons.append(poly)
            poly = []
    return (polygons)






def main():
    imagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\tPrism\\6_points.csv"
    # image = cv2.imread(imagePath)
    # #Select number of faces
    # value = face_amount(image)
    # #Extract polygons
    # polygons = extract_polygons(image, value)
    # print(polygons)
    lists = extract_polygons_csv(imagePath)
    print(len(lists))
    


[
[(333.78571428571433, 71.44805194805184), (224.69480519480518, 144.1753246753246), (332.48701298701303, 176.64285714285705), (411.7077922077922, 141.57792207792198)], 
[(319.5, 154.56493506493496), (253.26623376623374, 225.9935064935064), (376.6428571428571, 276.6428571428571), (441.57792207792204, 218.20129870129864)], 
[(455.8636363636364, 238.98051948051943), (345.47402597402595, 333.7857142857142), (418.2012987012987, 350.66883116883116), (518.2012987012987, 284.4350649350649)]]


if __name__ == "__main__":
    main()
