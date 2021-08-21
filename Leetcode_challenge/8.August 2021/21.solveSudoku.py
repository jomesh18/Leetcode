'''
Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

 

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.

'''
class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        not_solved = set()
        row = len(board)
        column = len(board[0])
        for i in range(row):
            for j in range(column):
                if board[i][j] == ".":
                    not_solved.add((i, j))

        def find_possible_values(i, j):
            print(i, j)
            sub_box_row, sub_box_column = (i//3)*3, (j//3)*3
            possible = set(range(1, 10))
            for k in range(sub_box_row, sub_box_row+3):
                for l in range(sub_box_column, sub_box_column+3):
                    current_val = board[sub_box_row][sub_box_column]
                    if current_val != '.' and sub_box_row != i and sub_box_column != j:
                        print(current_val, possible)
                        possible.remove(current_val)
            for k in range(row):
                if board[k][j] != "." and k != i:
                    if board[k][j] in possible:
                        possible.remove(board[k][j])
            for k in range(column):
                if board[i][k] != "." and k != j:
                    if board[i][k] in possible:
                        possible.remove(board[i][k])
            if len(possible) == 1:
                board[i][j] = possible.pop()
            else:
                not_solved.add((i, j))

        while not_solved:
            i, j = not_solved.pop()
            find_possible_values(i, j)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

sol = Solution()
sol.solveSudoku(board)
print(board)
print(board == Output)
