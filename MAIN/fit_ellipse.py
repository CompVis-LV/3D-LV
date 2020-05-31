import numpy as np
from pylab import *
import cv2
from createMask import select_polygon
from numpy.linalg import eig, inv

from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt

def fitEllipse(x,y):
    x = x[:,np.newaxis]
    y = y[:,np.newaxis]
    D =  np.hstack((x*x, x*y, y*y, x, y, np.ones_like(x)))
    S = np.dot(D.T,D)
    C = np.zeros([6,6])
    C[0,2] = C[2,0] = 2; C[1,1] = -1
    E, V =  eig(np.dot(inv(S), C))
    n = np.argmax(np.abs(E))
    a = V[:,n]
    return a

def ellipse_center(a):
    b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
    num = b*b-a*c
    x0=(c*d-b*f)/num
    y0=(a*f-b*d)/num
    return np.array([x0,y0])


def ellipse_angle_of_rotation( a ):
    b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
    return 0.5*np.arctan(2*b/(a-c))


def ellipse_axis_length( a ):
    b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
    up = 2*(a*f*f+c*d*d+g*b*b-2*b*d*f-a*c*g)
    down1=(b*b-a*c)*( (c-a)*np.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
    down2=(b*b-a*c)*( (a-c)*np.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
    res1=np.sqrt(up/down1)
    res2=np.sqrt(up/down2)
    return np.array([res1, res2])

def ellipse_angle_of_rotation2( a ):
    b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
    if b == 0:
        if a > c:
            return 0
        else:
            return np.pi/2
    else: 
        if a > c:
            return np.arctan(2*b/(a-c))/2
        else:
            return np.pi/2 + np.arctan(2*b/(a-c))/2


def main():
    image = cv2.imread('C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\user\\0_depth.png')
    height,width,depth = image.shape
    arc = 0.8
    R = np.arange(0,arc*np.pi, 0.01)
    x = 1.5*np.cos(R) + 2 + 0.1*np.random.rand(len(R))
    y = np.sin(R) + 1. + 0.1*np.random.rand(len(R))
    polygon = select_polygon(image)
    x = []
    y = []
    if len(polygon) < 5:
        return
    for i in range(5):
        x.append(polygon[i][0])
        y.append(polygon[i][1])
    x = np.array(x)
    y = np.array(y)
    print(x)
    print(y)
    a = fitEllipse(x,y)
    center = ellipse_center(a)
    #phi = ellipse_angle_of_rotation(a)
    phi = ellipse_angle_of_rotation2(a)
    axes = ellipse_axis_length(a)
    # get the individual axes
    a, b = axes
    ell = Ellipse(center, 2 * a, 2 * b,  phi * 180 / np.pi + 90 )
    print(ell)
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.add_artist(ell)
    ell.set_clip_box(ax.bbox)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    plt.show()
    scat = plt.scatter(x, y, c = "r")



if __name__ == "__main__":
    main()