def fitCircle():
    import numpy as np
    import argparse
    import cv2
    import signal

    from functools import wraps
    import errno
    import os
    import copy

    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    # args = vars(ap.parse_args())

    #image = cv2.imread(args["image"])
    image = cv2.imread("")
    
    orig_image = np.copy(image)
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    if(depth.type() != CV_32FC1)
            depth.convertTo(depth, CV_32FC1);

    Mat normals(depth.size(), CV_32FC3);

    for(int x = 0; x < depth.rows; ++x)
    {
        for(int y = 0; y < depth.cols; ++y)
        {
            // use float instead of double otherwise you will not get the correct result
            // check my updates in the original post. I have not figure out yet why this
            // is happening.
            float dzdx = (depth.at<float>(x+1, y) - depth.at<float>(x-1, y)) / 2.0;
            float dzdy = (depth.at<float>(x, y+1) - depth.at<float>(x, y-1)) / 2.0;

            Vec3f d(-dzdx, -dzdy, 1.0f);

            Vec3f n = normalize(d);
            normals.at<Vec3f>(x, y) = n;
        }
    }

    imshow("normals", normals);