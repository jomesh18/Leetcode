'''
37. Sudoku Solver
Solved
Hard
Topics
premium lock icon
Companies
Hint
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
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set(str(i) for i in range(1, 10)) for _ in range(9)]
        cols = [set(str(i) for i in range(1, 10)) for _ in range(9)]
        sqs = [set(str(i) for i in range(1, 10)) for _ in range(9)]
        to_fill = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': 
                    to_fill.append((i, j))
                else:
                    rows[i].remove(str(board[i][j]))
                    cols[j].remove(str(board[i][j]))
                    sqs[(i//3)*3+j//3].remove(str(board[i][j]))

        def dfs(k):
            if k == len(to_fill): return True
            i, j = to_fill[k]
            nums = rows[i] & cols[j] & sqs[(i//3)*3+j//3]
            for num in nums:
                board[i][j] = num
                rows[i].remove(num)
                cols[j].remove(num)
                sqs[(i//3)*3+j//3].remove(num)

                if dfs(k+1):
                    return True
                board[i][j] = '.'
                rows[i].add(num)
                cols[j].add(num)
                sqs[(i//3)*3+j//3].add(num)
            return False

        for k in range(len(to_fill)):
            if dfs(k):
                return board
