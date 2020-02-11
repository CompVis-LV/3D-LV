
import capture_frames as cf
import serial_angle as sa

location = '/////////////'


for ang = 1:200

    cont = sa.serialAngle(ang)

    if cont != True
        print("Error changing angle")
        break

    print("Environment Ready")
    cf.captureFrames(ang, location)
    print("Done")


