#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# Nathan Glikman
# 06/20/19
# Picross.py
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from PIL import Image
import numpy as np


def makeArrayFromBoard(image, width, height):

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
    
    return pixel_values

def getHints(board, line):
	
	hintArr = []

	count = 0
	for j in range(len(board[line])):
		
		if (board[line][j][0] == 0):
			count += 1
		elif (count != 0):
			hintArr.append(count)
			count = 0
	
	if (count != 0):
		hintArr.append(count)

	return hintArr

def main():
    
	image = Image.open('board.png', 'r')

	width, height = image.size
	board = makeArrayFromBoard(image, width, height)

	hints = [0] * width
	for i in range(len(board)):
		hints[i] = getHints(board, i)

	print(hints)

if __name__== '__main__': main()




