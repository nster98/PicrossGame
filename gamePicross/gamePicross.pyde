# Graphics part of picross

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
    newArr = [[0] * w for i in range(w)]
    k = 0
    
    for i in range(w):
        for j in range(h):
            if (k < len(arr)):
                newArr[i][j] = arr[k]
                k += 1
    
    return newArr

def setup():
    
    size(1200,800)
    
    image = loadImage("../board.png")
    _width, _height = image.width, image.height
    
    board = makeBoard(image, _width, _height)
    board = make2dArray(board, _width, _height)
    
    hints = [0] * (_width + _height)
    
    for i in range(len(board)):
        hints[i] = getHintsHorizontal(board, i)
    for i in range(len(board)):
        hints[_width + i] = getHintsVertical(board, i)
        
    print hints
            
    
#def draw():
    
