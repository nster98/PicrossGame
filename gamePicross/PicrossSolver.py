#~~~~~~~~~~~~~~~~~~~~~
# Nathan Glikman
# 06/24/19
# Picross Solver
# TODO: Get to work in main module
#~~~~~~~~~~~~~~~~~~~~~

# Active square: -1 (From grid)

def solve(grid, hints):
    
    x, y = 0, 0
    for i in range(len(hints) / 2):
        count = 0
        for j in range(len(hints[i])):
            if count < hints[i][j]:
                grid[x][y] = -1
            else:
                y += 1
            y += 1
        y = 0
        x += 1
        
    return grid

def instantSolve(board, grid):
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] != -1:
                grid[x][y] = -1
                
    return grid
