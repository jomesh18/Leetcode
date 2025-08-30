'''
36. Valid Sudoku
Solved
Medium
Topics
premium lock icon
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(r):
            row = [0]*9
            for i in range(9):
                if board[r][i] != '.':
                    curr = int(board[r][i])-1
                    if row[curr] == 1:
                        return False
                    row[curr] = 1
            return True

        def check_col(c):
            col = [0]*9
            for i in range(9):
                if board[i][c] != '.':
                    curr = int(board[i][c])-1
                    if col[curr] == 1:
                        return False
                    col[curr] = 1
            return True

        def check_sub(pos):
            r_start = (pos // 3) * 3
            c_start = (pos % 3 ) * 3
            full = [0]*9
            for i in range(r_start, r_start+3):
                for j in range(c_start, c_start+3):
                    if board[i][j] != '.':
                        curr = int(board[i][j])-1
                        if full[curr] == 1:
                            return False
                        full[curr] = 1
            return True

        for i in range(9):
            if not check_row(i):
                return False

        for i in range(9):
            if not check_col(i):
                return False

        for i in range(9):
            if not check_sub(i):
                return False

        return True
