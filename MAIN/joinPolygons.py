import numpy as np
import argparse
import cv2
import scipy.spatial as spatial

def join_polygons(faces, value):
    for fc in range(value):
        for a in range(value):
            if fc != a:
                for x in range(len(faces["%s" % (fc)]['polygon'])):
                    point_tree = spatial.cKDTree(faces["%s" % (a)]['polygon'])
                    common = (point_tree.query_ball_point(faces["%s" % (fc)]['polygon'][x], 20))
                    for c in range(len(common)):
                        print("start change")
                        p1 = faces["%s" % (fc)]['polygon'][x]
                        p2 = faces["%s" % (a)]['polygon'][common[c]]
                        print(p1)
                        print(p2)
                        #ADD moves to closest point it joins with, cant move to a point it already is at
                        avg = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
                        print(avg)
                        faces["%s" % (fc)]['polygon'][x] = avg
                        faces["%s" % (a)]['polygon'][common[c]] = avg
                        faces["%s" % (fc)]["joins"].append(a)
    return(faces)


def main():
    faces = {'0': {'polygon': [(335.08441558441564, 70.14935064935054), (200.01948051948048, 137.68181818181807), 
    (366.2532467532468, 233.78571428571422), (489.62987012987014, 136.38311688311683)], 
    'joins': []}, '1': {'polygon': [(198.72077922077924, 142.8766233766233), (215.60389610389612, 251.9675324675324), 
    (358.461038961039, 337.68181818181813), (362.3571428571429, 231.18831168831161)], 'joins': []}, 
    '2': {'polygon': [(362.3571428571429, 228.590909090909), (492.22727272727275, 133.78571428571422), (467.5519480519481, 
    241.57792207792204), (359.7597402597403, 341.57792207792204)], 'joins': []}}
    print(faces)
    value = 3
    joinedFaces = join_polygons(faces, value)
    print(joinedFaces)

if __name__ == "__main__":
    main()





