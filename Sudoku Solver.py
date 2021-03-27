"""
This application will solve a Sudoku board. The empty cells are indicated as 0. 
"""

class SudokuSolver(object):
    
    # create Sudoku board
    def __init__(self, board):
        self.board = board
        
    # show board
    def __str__(self):
        show_board = ""

        for i in range(9):
            row = ''

            for j in range(9):
                if j % 3 == 0:
                    row += " |"
                row += (" " + str(self.board[i][j]))
            show_board += (row + " |")
            
            if i == 2 or i == 5:
                show_board += ("\n " + (len(row) + 1) * "-" + "\n")
            else:
                show_board += "\n"
                
        return show_board
    
    
    # check each cell to see if it is valid, at the end, the board should be solved.
    def solve_sudoku(self):
        
        # find empty cell
        empty = self.find_empty()    
        
        # this indicates that we have gone through the whole board and is exit entry (base case).
        if not empty:
            return True
        else: # otherwise unpack tuple to row and column
            row, col = empty
        
        # if empty fill in cell and check to see if it is valid
        for val in range(1, 10):
            if self.check_valid(row, col, val) == True:
                self.board[row][col] = val
                
                # recursively go through the board
                if self.solve_sudoku() == True:
                    return True
                
        # if none of the values work, clear the cell.
        self.board[row][col] = 0
        
        return False
        
        
    
    # find empty cell
    def find_empty(self):
        
        # go through the board
        for row in range(9):
            for col in range(9):
            
                # check to see if cell is empty and return position
                if self.board[row][col] == 0:
                    return (row, col)
        
        # return this if there are no more empty cells.
        return None
    
        
    # check each cell to see if it is valid.    
    def check_valid(self, row, col, val):
        
        # check validiy of val horizontally
        for h in range(9):
            
            # this will indicate that the value chosen does not work
            if val == self.board[row][h] and h != col:
                return False
        
        # check validiy of val vertically
        for v in range(9):
            
            # this will indicate that the value chosen does not work
            if val == self.board[v][col] and v != row:
                return False
            
        # check validity of val in box
        for i in (range((row//3)*3, (row//3)*3+3)):
            for j in (range((col//3)*3, (col//3)*3+3)):
                if val == self.board[i][j]:
                    return False
            
        return True
            

# solve a board, 0 is the empty space that needs to be solved.
board = SudokuSolver([
    [0, 9, 4, 0, 3, 0, 1, 0, 0],
    [8, 1, 2, 7, 0, 0, 0, 9, 6],
    [3, 0, 0, 1, 9, 0, 0, 0, 0],
    [0, 3, 0, 9, 0, 4, 6, 0, 0],
    [0, 0, 8, 6, 1, 3, 0, 4, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [4, 0, 3, 5, 0, 0, 0, 0, 8],
    [5, 0, 0, 0, 2, 0, 7, 0, 0],
    [0, 6, 0, 0, 0, 8, 4, 1, 5]])

board.solve_sudoku()
print(board)