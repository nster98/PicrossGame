#~~~~~~~~~~~~~~~~~~~~~
# Nathan Glikman
# 06/24/19
# Picross Tools
#~~~~~~~~~~~~~~~~~~~~~

def makeBoard(img, w, h):
    
    boardArr = []
    
    img.loadPixels()
    
    for x in range(w * h):
        boardArr.append(img.pixels[x])
        
    return boardArr

def getHintsHorizontal(board, i):

    hintsArr = []
    count = 0
    
    for j in range(len(board[i])):
        if (board[i][j] != -1):
            count += 1
        elif (count != 0):
            hintsArr.append(count)
            count = 0
    
    if (count != 0):
        hintsArr.append(count)
        
    return hintsArr
def getHintsVertical(board, i):

    hintsArr = []
    count = 0
    
    for j in range(len(board[i])):
        if (board[j][i] != -1):
            count += 1
        elif (count != 0):
            hintsArr.append(count)
            count = 0
    
    if (count != 0):
        hintsArr.append(count)
        
    return hintsArr

def make2dArray(arr, w, h):
    newArr = [[0] * w for i in range(h)]
    k = 0
    
    for i in range(w):
        for j in range(h):
            if (k < len(arr)):
                newArr[i][j] = arr[k]
                k += 1
    
    return newArr
