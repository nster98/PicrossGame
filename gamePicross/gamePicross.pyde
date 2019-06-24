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
    newArr = [[0] * w for i in range(h)]
    k = 0
    
    for i in range(w):
        for j in range(h):
            if (k < len(arr)):
                newArr[i][j] = arr[k]
                k += 1
    
    return newArr

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

board = []
grid = []
hints = []
_width = 0
_height = 0

def setup():
    
    size(1200,800)
    
    global hints, board, grid, _width, _height
    
    image = loadImage("../bird.png")
    _width, _height = image.width, image.height
    
    board = makeBoard(image, _width, _height)
    board = make2dArray(board, _width, _height)

    grid = [[1] * _width for i in range(_height)]
    
    hints = [0] * (_width + _height)
    
    for i in range(len(board)):
        hints[i] = getHintsHorizontal(board, i)
    for i in range(len(board)):
        hints[_width + i] = getHintsVertical(board, i)
        
    print hints
    
            
def draw():
    
    global hints, board, grid, _width, _height
    w, h = _width*3, _height*3
    
    x, y = 0, 0
    for row in grid:
        for col in row:
            if col == -1:
                fill(0)
            elif col == 2:
                fill(255,165,0)
            else:
                fill(255)
            rect(x, y, w, h)
            x = x + w
        y = y + h
        x = 0

    textX, textY = w * _width + 5, h - 10
    fill(0)
    textSize(32)
    for i in range(len(hints) / 2):
        for j in range(len(hints[i])):
            text(hints[i][j], textX, textY)
            textX += 30
        textX = w * _width + 5
        textY += h

    textX, textY = 10, h * _height + 30
    for i in range(len(hints) / 2):
        for j in range(len(hints[i + _width])):
            text(hints[i + _width][j], textX, textY)
            textY += 30
        textY = h * _height + 30
        textX += w
     
        
def mousePressed():
    
    global board, grid, _width, _height
    w, h = _width*3, _height*3
    
    if (mouseButton == LEFT and mouseX < w * _width and mouseY < h * _height):
        if (grid[int(mouseY/h)][int(mouseX/w)] == 2):
            grid[int(mouseY/h)][int(mouseX/w)] = 1
        else:
            grid[int(mouseY/h)][int(mouseX/w)] *= -1
        
    if (mouseButton == RIGHT and mouseX < w * _width and mouseY < h * _height):
        if (grid[int(mouseY/h)][int(mouseX/w)] != 2):
            grid[int(mouseY/h)][int(mouseX/w)] = 2
        else:
            grid[int(mouseY/h)][int(mouseX/w)] = 1
