# Graphics part of picross

import PicrossTools
import PicrossSolver

board = []
grid = []
hints = []
_width = 0
_height = 0

translateAmount = 400

def setup():
    
    size(1200,800)
    
    global hints, board, grid, _width, _height
    
    image = loadImage("../pictures/bird.png")
    _width, _height = image.width, image.height
    
    board = PicrossTools.makeBoard(image, _width, _height)
    board = PicrossTools.make2dArray(board, _width, _height)

    grid = [[1] * _width for i in range(_height)]
    
    hints = [0] * (_width + _height)
    
    for i in range(len(board)):
        hints[i] = PicrossTools.getHintsHorizontal(board, i)
    count = 0
    for i in range(len(board[0])):
        hints[_height + count] = PicrossTools.getHintsVertical(board, i)
        count += 1
    
    print hints
    
            
def draw():
    
    # Active square: -1
    
    global hints, board, grid, _width, _height, translateAmount
    
    translate(translateAmount, 0)
    w, h = _width*3, _height*3
    
    x, y = 0, 0
    for row in grid:
        for col in row:
            fill(255)
            rect(x, y, w, h)
            if col == -1:
                fill(0)
            elif col == 2:
                fill(255,165,0)
            else:
                fill(255)
            rect(x+2, y+2, w-4, h-4)
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
        for j in range(len(hints[i + _height])):
            text(hints[i + _height][j], textX, textY)
            textY += 30
        textY = h * _height + 30
        textX += w
    
    #grid = PicrossSolver.instantSolve(board, grid)
    #grid = PicrossSolver.solve(grid, hints)
    
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
