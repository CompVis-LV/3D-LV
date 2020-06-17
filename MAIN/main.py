import numpy as np
import argparse
import cv2
import scipy
import csv
import os
import math
import itertools as it
import createMask as cm
import extractPolygons as ep
import normal2 as n
import fillHoles as fh
import joinPolygons as jp

def create_dict(polygons, value):
    faces = {}
    for count in range(value):
        thisdict = dict(polygon=polygons[count], joins=[], angle=[])
        faces["%s" % (count)] = thisdict
    return faces

def extract_planes(normals, faces, value):
    imageAv = normals.copy()
    for count in range(value):
        r, depth = cm.create_mask(normals, faces["%s" % (count)]['polygon'])
        imageAv, v = cm.replace_masked_average(r, imageAv)
        faces["%s" % (count)]["vector"] = v
        #Preview plane creation, image isnt actually saved, vector (v) saved to dictionary
        cv2.imshow("Masked average", imageAv)
        cv2.waitKey(0)
    return faces, imageAv

#https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python/13849249#13849249
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def truncate(n, binSize, decimals=0):
    multiplier = binSize ** decimals
    return int(n * multiplier) / multiplier

def convert_degree_bins(angle, binSize = 10):
    deg = math.degrees(angle)
    deg = truncate(deg, binSize, -1)
    return deg

def find_angle_between(faces, grdVec):
    for x in faces:
        faces[x]["angle"].append(convert_degree_bins(angle_between(faces[x]['vector'], grdVec), 30))
        for j in faces[x]['joins']:
            v1 = faces[x]['vector']
            v2 = faces["%s" % (j)]['vector']
            faces[x]["angle"].append(convert_degree_bins(angle_between(v1, v2), 30))
    return faces


def csv_write_raw(faces, filename = "file.csv"):
    allrows = []
    for face, name in faces.items():
        print(face)
        print(name)
        rows = list(it.zip_longest(name['polygon'], name['joins'], name['angle'], name['vector'], fillvalue=''))
        print("rows = ", rows)
        for i in range(len(rows)):
            if i:
                rows[i] = ('',) + rows[i]
            else:
                rows[i] = (face,) + rows[i]
        allrows.extend(rows)
    with open(filename, 'w') as fd:
        csv_columns = ['face','polygon','joins', 'angle', 'vector']
        writer = csv.writer(fd)
        writer.writerow(csv_columns)
        for row in allrows:
            writer.writerow(row)

def csv_write_pl(faces, filename = "file.csv"):
    allrows = []
    count = 0
    for face, name in faces.items():
        print(face)
        print(name)
        print(count)
        allrows.append([face, len(name['polygon']), name['joins'], name['angle'], name['vector']])
        count += 1
        print("rows = ", allrows)

    with open(filename, 'w') as fd:
        csv_columns = ['face','sides','joins', 'angle', 'vector']
        writer = csv.writer(fd)
        writer.writerow(csv_columns)
        for row in allrows:
            writer.writerow(row)

def ground_vector():
    colourImagePath = "0_colour.png"
    depthImagePath = "0_depth.png"
    image = cv2.imread(colourImagePath)
    depthImageHoley = cv2.imread(depthImagePath)
    depthImage = fh.fill_holes(depthImageHoley)
    polygons = ep.extract_polygons(image, 1)
    normals, itm = n.extract_normals(depthImage)
    normals = n.remove_noise_layer(normals, itm)
    faces = create_dict(polygons, 1)
    faces, image = extract_planes(normals, faces, 1)
    print(faces)
    return faces['0']['vector']




def main():
    os.chdir(r"C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\cube")
    grdV = ground_vector()
    for x in range(0, 43, 2):
        #IMPORT IMAGE
        x = 12
        colourImagePath = "%s_colour.png" % (x)
        depthImagePath = "%s_depth.png" % (x)
        #colourImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\hexagon.png"
        #depthImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\hexagon.png"
        image = cv2.imread(colourImagePath)

        #FILL MISSING DATA IN DEPTH IMAGE
        #depthImage = cv2.imread(depthImagePath)
        # depthImageHoley = cv2.imread(depthImagePath)
        # depthImage = fh.fill_holes(depthImageHoley)
        depthImage = cv2.imread(depthImagePath)
        # cv2.imshow("Start Image", image)
        # cv2.waitKey(0)
        # cv2.imshow("Start Image", depthImage)
        # cv2.waitKey(0)
        #CREATE MASK
        mask = image.copy()
        layers = 0
        mask, layers = cm.create_mask(image)
        cv2.imwrite( "%s_mask.png" % (x), (mask*255).astype(np.uint8))
        maskedImage = cm.mask_off(mask, image)
        cv2.imwrite( "%s_maskedImage.png" % (x), (maskedImage).astype(np.uint8))
        maskedDepthImage = cm.mask_off(mask, depthImage)
        cv2.imwrite( "%s_maskedDepthImage.png" % (x), (maskedDepthImage).astype(np.uint8))
        #EXTRACT POLYGONS
        value = ep.face_amount(maskedImage)
        polygons = ep.extract_polygons(maskedImage, value)

        # Create dictionary to link infomration
        faces = create_dict(polygons, value)

        #LINK POLYGON EDGES - Identify joining polygons
        faces = jp.join_polygons(faces, value) 

        #EXTRACT NORMALS
        normals, itm = n.extract_normals(maskedDepthImage)
        normals = n.remove_noise_layer(normals, itm) #much worse without noise reduction

        #EXTRACT PLANES
        faces, image = extract_planes(normals, faces, value)
        cv2.imwrite( "%s_planes.png" % (x), (image*255).astype(np.uint8))
        cv2.destroyAllWindows()
        #EXTRACT DATA to CSV etc
        faces =  find_angle_between(faces, grdV)
        print(faces)
        csv_write_pl(faces, filename = "%s_file.csv" % (x))
        


if __name__ == "__main__":
    main()
