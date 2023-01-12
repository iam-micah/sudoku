# ===========================================================================
#  Micah Akai-Nettey (sakain01)
#  CS 131 Spring 2022
#  Assignment 4, CSP 
#
#  Purpose:
#      Solve a sudoku puzzle
#
#  Notes:
#      1. This program models the puzzle as a CSP
#      2. This program uses backtracking to solve the puzzle
#      3. The constraints we're using in this solution are: 
#         non duplication across rows, columns, and 3x3 grid boxes
#
#  ChangeLog:
#      04/20/2022: sakain01
#           newsudoku.py file created
# ===========================================================================

# ===========================================================================
#                            Function Definitions
# ===========================================================================

# print_grid_helper
#    Purpose: create a helper function that displays the grid to the terminal
# Parameters: input_grid -> array representation of sudoku puzzle
#    Returns: none
#
#      Notes: style choice opted for was minimalist for the grid display
#             To suit the normal sudoku style, imagine divisions after 
#             every third entry, so that the grid can be perfectly divided
#             into lines
def print_grid_helper(input_grid):
    for row in range(9):
        for col in range(9):
            print (input_grid[row][col], end = " ")
        print ()

# empty
#    Purpose: finds the entry in the grid that has still not been filled
# Parameters: input_grid ->  array representation of sudoku puzzle
#             list       ->  keeps track of incrementation of rows and columns
#    Returns: boolean
#
#      Notes: Searches the grid to find an unassigned entry
#             If an empty location is found, True is returned
#             This helps the solve_puzzle function to know which positions
#             have been filled
def empty(input_grid, list):
    for row in range(9):
        for col in range(9):
            if(input_grid[row][col]== 0):
                list[0]= row
                list[1]= col
                return True
    return False


# in_row
#    Purpose: verifies row entry for our constraint
# Parameters: input_grid ->  array representation of sudoku puzzle
#             row        ->  row to be searched
#             num        ->  number to be verified
#    Returns: boolean
#
#      Notes: Searches the grid to find an unassigned entry
#             If an empty location is found, True is returned
#             This helps the solve_puzzle function to know which positions
#             have been filled in a row
def in_row(input_grid, row, num):
    for i in range(9):
        if(input_grid[row][i] == num):
            return True
    return False

# in_col
#    Purpose: verifies column entry for our constraint
# Parameters: input_grid ->  array representation of sudoku puzzle
#             col        ->  column to be searched
#             num        ->  number to be verified
#    Returns: boolean
#
#      Notes: Searches the grid to find an unassigned entry
#             If an empty location is found, True is returned
#             This helps the solve_puzzle function to know which positions
#             have been filled in a column
def in_col(input_grid, col, num):
    for i in range(9):
        if(input_grid[i][col] == num):
            return True
    return False


# in_col
#    Purpose: verifies box entry for our constraint
# Parameters: input_grid ->  array representation of sudoku puzzle
#             row        ->  row to be searched
#             col        ->  column to be searched
#             num        ->  number to be verified
#    Returns: boolean
#
#      Notes: Searches the grid to find an unassigned entry
#             If an empty location is found, True is returned
#             This helps the solve_puzzle function to know which positions
#             have been filled in a box
#             box is a 3 x 3 fixed position
def in_box(input_grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if(input_grid[i + row][j + col] == num):
                return True
    return False


# legal
#    Purpose: verifies whether a new entry can be legal in a location
# Parameters: input_grid ->  array representation of sudoku puzzle
#             row        ->  row to be searched
#             col        ->  column to be searched
#             num        ->  number to be verified
#    Returns: boolean
#
#      Notes: None
def legal(input_grid, row, col, num):

    # Check if 'num' is present in our constraints
    return not in_row(input_grid, row, num) and not in_col(input_grid, col, num) and not in_box(input_grid, row - row % 3,
                        col - col % 3, num)


# solve puzzle
#    Purpose: takes an input grid (which should ideally be partially filled)
#             and attempts to assign values to all empty (or unassigned) 
#             locations so as to satisfy our constraints
# Parameters: input_grid ->  array representation of sudoku puzzle
#             row        ->  row to be searched
#             col        ->  column to be searched
#             num        ->  number to be verified
#    Returns: boolean
#
#      Notes: uses recursion
def solve_puzzle(input_grid):

    # keeps track of rows and columns in the empty function
    list =[0, 0]

    # If all locations are filled, we are done solving the puzzle
    if(not empty(input_grid, list)):
        return True

    # Assign list values
    row = list[0]
    col = list[1]

    # use only digits (1 to 9)
    for num in range(1, 10):
        
        # If constraints are satisfied
        if(legal(input_grid, row, col, num)):
            
            # use a temporary assignment 
            input_grid[row][col]= num

            # if assignment was a success, recursively solve the remaining
            # slots
            if(solve_puzzle(input_grid)):
                return True

            # if assignment was a failure, reset and try new assignment
            input_grid[row][col] = 0
            
    # Backtracking
    return False

# Driver code to test the functions
if __name__=="__main__":

    # create 2D array for grid (use list comprehension)
    grid =[[0 for x in range(9)] for y in range(9)]
    
    # assign iniital fixed values to our grid
    grid =[[6, 0, 8, 7, 0, 2, 1, 0, 0],
           [4, 0, 0, 0, 1, 0, 0, 0, 2],
           [0, 2, 5, 4, 0, 0, 0, 0, 0],
           [7, 0, 1, 0, 8, 0, 4, 0, 5],
           [0, 8, 0, 0, 0, 0, 0, 7, 0],
           [5, 0, 9, 0, 6, 0, 3, 0, 1],
           [0, 0, 0, 0, 0, 6, 7, 5, 0],
           [0, 0, 0, 0, 9, 0, 0, 0, 8],
           [0, 0, 6, 8, 0, 5, 2, 0, 3]]

    # print previous grid
    print("Sudoku puzzle:")
    print_grid_helper(grid)
    print("")
    print("------------------")
    print("")
    # if success print the grid
    if(solve_puzzle(grid)):
        print("Solved: ")
        print_grid_helper(grid)
    else:
        print ("Unsolvable grid")
