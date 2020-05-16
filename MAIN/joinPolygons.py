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
                        faces["%s" % (fc)]["joins"].add(a)
    return(faces)


def main():
    faces = {'0': {'polygon': [(333.78571428571433, 70.14935064935054), (198.72077922077924, 142.8766233766233), 
    (363.6558441558442, 229.8896103896103), (489.62987012987014, 138.98051948051938)], 'joins': set()}, 
    '1': {'polygon': [(201.31818181818178, 145.4740259740259), (214.30519480519482, 253.2662337662337), 
    (355.8636363636364, 344.17532467532465), (366.2532467532468, 227.2922077922077)], 'joins': set()}, 
    '2': {'polygon': [(468.8506493506494, 240.27922077922074), (488.33116883116884, 137.68181818181807), 
    (366.2532467532468, 229.8896103896103), (358.461038961039, 342.87662337662334)], 'joins': set()}}
    print(faces)
    value = 3
    joinedFaces = join_polygons(faces, value)
    print(joinedFaces)

if __name__ == "__main__":
    main()





