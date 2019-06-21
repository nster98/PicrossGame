#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# Nathan Glikman
# 06/20/19
# Picross.py
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from PIL import Image
import numpy as np


def makeArrayFromBoard(image):

    width, height = image.size
    pixel_values = list(image.getdata())
    
    if image.mode == 'RGBA':
        channels = 4
    elif image.mode == 'RGB':
        channels = 3
    elif image.mode == 'L':
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None

    pixel_values = np.array(pixel_values).reshape((width, height, channels))
    
    print("We got here  boys")

    return pixel_values

def main():
    
    image = Image.open('board.png', 'r')

    makeArrayFromBoard(image)

if __name__== '__main__': main()




