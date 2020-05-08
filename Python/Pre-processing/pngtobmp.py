

def main(file = "C:\\Users\\Jared\\Documents\\ECTE458\\3D-LV\\Datasets\\test8\\"):
    import os

    for filename in os.listdir(file):
        if filename.endswith("depth.png"): 
            pngtobmp(file + filename, file + (filename[:-4] + ".bmp"))
            continue
        else:
            continue

def pngtobmp(infile, outfile):
    import imutils
    import cv2
    from PIL import Image

    #img = Image.open(infile)
    img = cv2.imread(infile)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = imutils.resize(img, width=160)
    cv2.imwrite(outfile, img)

    image = Image.open(outfile)
    newimg = image.convert(mode='P', colors=8)
    image.close()
    newimg.save(outfile)


if __name__ == "__main__":
    main()