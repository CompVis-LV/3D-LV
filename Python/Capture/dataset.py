
import capture_frames as cf
import serial_angle as sa
import time
import os
import cv2

# define the name of the directory to be created
path = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\test15\\"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)

else:
    print ("Successfully created the directory %s " % path)

    location = path

    cf.captureFrames()
    im = cv2.imread("0_depth.png")
    # Select ROI
    r = cv2.selectROI(im)
    print(r[0])
    print(r[1])
    print(r[2])
    print(r[3])

    for ang in range(12):
        ang = ang*2
        cont = False
        cont = sa.serialAngle(20)
        time.sleep(2)
        print(cont)

        if cont == False:
            print("Error changing angle")
            break

        print("Environment Ready")
        cf.captureFrames(r, ang, location)

        time.sleep(2)
        print("Done")


