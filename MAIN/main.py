import numpy as np
import argparse
import cv2
import scipy
import createMask as cm
import extractPolygons as ep
import normal2 as n
import fillHoles as fh
import joinPolygons as jp

#https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python/13849249#13849249
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def main():
    #IMPORT IMAGE
    #colourImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\test7\\2_colour.png"
    #depthImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\test7\\2_depth.png"
    colourImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\hexagon.png"
    depthImagePath = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\hexagon.png"
    image = cv2.imread(colourImagePath)
    depthImageHoley = cv2.imread(depthImagePath)
    depthImage = fh.fill_holes(depthImageHoley)
    cv2.imshow("Start Image", image)
    cv2.waitKey(0)
    #CREATE MASK
    mask = image.copy()
    layers = 0
    mask, layers = cm.create_mask(image)
    maskedImage = cm.mask_off(mask, image)
    maskedDepthImage = cm.mask_off(mask, depthImage)
    # cv2.imshow("Masked Image", maskedImage)
    # cv2.waitKey(0)
    #EXTRACT POLYGONS
    value = ep.face_amount(maskedImage)
    polygons = ep.extract_polygons(maskedImage, value)
    # Create dictionary to link infomration
    faces = {}
    for count in range(value):
        thisdict = dict(polygon=polygons[count], joins=set())
        faces["%s" % (count)] = thisdict
    print(faces)
    #LINK POLYGON EDGES - Identify joining polygons
    faces = jp.join_polygons(faces, value)
    print(faces)
    #EXTRACT NORMALS
    #Read depth image
    normals, itm = n.extract_normals(maskedDepthImage)
    #EXTRACT PLANES
    imageAv = normals.copy()
    for count in range(value):
        r, depth = cm.create_mask(normals, polygons[count])
        imageAv, v = cm.replace_masked_average(r, imageAv)
        faces["%s" % (count)]["vector"] = v
        cv2.imshow("Masked average", imageAv)
        cv2.waitKey(0)
    #LINK POLYGON AND PLANE INFO
    # EACH FACE - Polygon vertices, joining faces, angle between planes  
    #EXTRACT DATA to CSV etc
    print(faces)
    # joining faces
    for i in range(value):
        for j in range(value):
            if i !=j:
                faces["%s" % (count)]["Angle"] = angle_between(v1, v2)

if __name__ == "__main__":
    main()
