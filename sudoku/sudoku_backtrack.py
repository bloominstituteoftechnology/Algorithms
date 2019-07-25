#!/home/tt/anaconda3/bin/python
'''

'''

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' ')
        print('n')

def used_in_row(grid,row,num):
    for c in range(9):
        if grid[row][c] == num :
            return True 
    return False

def used_in_col(grid,col,num):
    for r in range(9):
        if grid[r][col] == num:
            return True
    return False

def used_in_3x3(grid,row,col,num):
    row = row - row%3
    col = col - col%3
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col] == num:
                return True
    return False

def valid_loc(g,r,c,n):
    return not used_in_row(g,r,n) and\
        not used_in_col(g,c,n) and not used_in_3x3(g,r,c,n)
        
'''
build an adjacency list of empty slot with available number
{ (i,j): [1,2,3,4,5,6,7,8,9]}
'''
def find_an_empty_slot(grid,l):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                l[0] = i
                l[1] = j
                return True

    return False


def solve_sudoku(grid):
    l = [0,0]
    if not find_an_empty_slot(grid,l):
        return True # finish 

    row=l[0]
    col=l[1]

    for num in range(1,10):
        if valid_loc(grid,row,col,num):
            grid[row][col]=num
            if solve_sudoku(grid):
                print(f'row={row} col={col} num={num}')
                return True
            grid[row][col] = 0
    return False




if __name__ == "__main__":
    # create two dimensional 9x9 grid
    grid = [[0 for x in range(9)] for y in range(9)]

    # assigning values to the grid 
    grid=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] 

    # if success print the grid 
    if(solve_sudoku(grid)): 
        print_grid(grid) 
        
    else: 
        print("No solution exists")