import numpy as np
from PIL import Image

## This code was adapted from the book Python Playground.
## by Mahesh Venkitachalam
## nostarch.com

## The code has been drasticly shortened for a summer camp.

gscale = "@%#*+=-:. "

def computeAverage(image):
    im = np.array(image)
    w,h = im.shape
    return np.average(im.reshape(w*h))

def convertImageToAscii(fileName, cols, scale):
    image = Image.open(fileName).convert('L')
    W, H = image.size
    print("input image dims: %d x %d" % (W, H))

    w = W // cols
    h = w // scale
    rows = int(H // h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    asciiImg = []
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        if j == rows-1:
            y2 = H
        asciiImg.append("")
        for i in range(cols):
            x1 = i * w
            x2 = (i + 1) * w
            if i == cols-1:
                x2 = W

            img = image.crop((x1, y1, x2, y2))
            avg = int(computeAverage(img))
            asciiImg[j] += gscale[int((avg*len(gscale))/255)]
    
    return asciiImg

def main():
    imgFile = input("Enter an filename to read: ")
    outFile = input("Enter the output file to write: ")

    scale = 0.43
    cols = 50

    print('generating ASCII art...')
    asciiImg = convertImageToAscii(imgFile, cols, scale)

    f = open(outFile, 'w')
    for row in asciiImg:
        f.write(row + '\n')

    f.close()
    print("ASCII art written to %s" % outFile)

main()
