
import capture_frames as cf
import serial_angle as sa

location = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\test\\"


for ang in range(5):
    ang = ang*2
    cont = sa.serialAngle(ang)

    print(cont)

    if cont != True:
        print("Error changing angle")
        break

    print("Environment Ready")
    #cf.captureFrames(ang, location)
    print("Done")


