import tkinter

"""
Wrapper for tkinter which I believe is easier to use for
drawing shapes than the standard API.

Any time 'color' is referenced, you may use a tkinter
hex color or a standard English color.

English defined colors: 'white', 'black', 'red',
'green', 'blue', 'cyan', 'yellow', and 'magenta'.

To use this wrapper:

    from shapes import *

    window = createCanvas(600, 600)
    drawRectangle(window, 25, 50, 125, 150, 'red')
    drawFilledRectangle(window, 175, 50, 275, 150, 'green')
    drawCircle(window, 375, 100, 50, 'blue')
    drawFilledCircle(window, 525, 100, 50, 'magenta')

    drawText(window, 300, 200, "This is a test of the drawText function.")
    drawLine(window, 100, 225, 500, 225, 'cyan')
    drawLine(window, 100, 250, 500, 250, 'yellow')
    drawLine(window, 100, 275, 500, 275, 'cyan')
    drawLine(window, 100, 300, 500, 300, 'yellow')

    drawTriangle(window, 75, 325, 100)
    drawTriangle(window, 225, 325, 100, 'purple')
    drawFilledTriangle(window, 375, 325, 100, 'orange')
    drawFilledTriangle(window, 525, 325, 100, 'brown')

    mainloop()

James Church
2014-09-08
"""

def createCanvas(width, height):
    """
    Creates a canvas on the screen of width by height size
    with a white backgorund color.
    """
    master = tkinter.Tk()
    window = tkinter.Canvas(master, width=width, height=height, background='white')
    window.pack()
    return window

def drawText(window, x, y, thistext, color='black'):
    """
    Draws text on the screen at an (x,y) coordinate.
    Default color is black.
    """
    window.create_text(x, y, text=thistext, fill=color)

def drawLine(window, startx, starty, endx, endy, color='black'):
    """
    Draws a line from start to end.
    Default color is black.
    """
    window.create_line(startx, starty, endx, endy, fill=color)

def drawCircle(window, cx, cy, radius, color='black'):
    """
    Draws an open circle with the center at a coordinate with a specified radius.
    Default color is black.
    """
    ulx = cx - radius
    uly = cy - radius
    lrx = cx + radius
    lry = cy + radius
    window.create_oval(ulx, uly, lrx, lry, outline=color)

def drawFilledCircle(window, cx, cy, radius, color='black'):
    """
    Draws a filled circle with the center at a coordinate with a specified radius.
    Default color is black.
    """
    ulx = cx - radius
    uly = cy - radius
    lrx = cx + radius
    lry = cy + radius
    window.create_oval(ulx, uly, lrx, lry, outline=color, fill=color)

def drawRectangle(window, ulx, uly, lrx, lry, color='black'):
    """
    Draws an open square with a bounding box specified by (ulx, uly, lrx, lry)
    ulx - upper left x
    uly - upper left y
    lrx - lower right x
    lry - lower right y
    Default color is black.
    """
    window.create_rectangle(ulx, uly, lrx, lry, outline=color)

def drawFilledRectangle(window, ulx, uly, lrx, lry, color='black'):
    """
    Draws a filled square with a bounding box specified by (ulx, uly, lrx, lry)
    ulx - upper left x
    uly - upper left y
    lrx - lower right x
    lry - lower right y
    Default color is black.
    """
    window.create_rectangle(ulx, uly, lrx, lry, outline=color, fill=color)

def drawTriangle(window, tx, ty, height, color='black'):
    splitSide = 0.57735 * height # Length of the opposite side is height*tan(30 degrees)
    ly = ty + height
    ry = ty + height
    lx = tx - splitSide
    rx = tx + splitSide

    window.create_polygon(tx, ty, lx, ly, rx, ry, outline=color, fill="")

def drawFilledTriangle(window, tx, ty, height, color='black'):
    splitSide = 0.57735 * height # Length of the opposite side is height*tan(30 degrees)
    ly = ty + height
    ry = ty + height
    lx = tx - splitSide
    rx = tx + splitSide

    window.create_polygon(tx, ty, lx, ly, rx, ry, outline=color, fill=color)

def mainloop():
    """
    Begins drawing our art.
    """
    tkinter.mainloop()
