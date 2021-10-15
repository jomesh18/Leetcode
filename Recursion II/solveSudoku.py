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
import pprint
class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        to_fill = [(i, j) for j in range(9) for i in range(9) if board[i][j] == "."]
        self.finished = False
        def backtrack():
            if not to_fill:
                self.finished = True
                return
            i, j = to_fill.pop()
            candidates = find_valid_candidates(i, j)
            for candidate in candidates:
                place_candidate(i, j, candidate)
                backtrack()
                if self.finished: return
                remove_candidate(i, j, candidate)
            to_fill.append((i, j))

        def place_candidate(i, j, candidate):
            board[i][j] = str(candidate)

        def remove_candidate(i, j, candidate):
            board[i][j] = "."

        def find_valid_candidates(i, j) -> [int]:
            row_start, column_start = (i//3)*3, (j//3)*3
            present_in_row = {int(board[i][l]) for l in range(9) if board[i][l] != "."}
            present_in_col = {int(board[l][j]) for l in range(9) if board[l][j] != "."}
            present_in_square = {int(board[k][l]) for k in range(row_start, row_start+3) for l in range(column_start, column_start+3) if board[k][l] != "."}
            present = present_in_square | present_in_row | present_in_col
            return list(set(i for i in range(1, 10))-present)

        backtrack()

#from leetcode
# from collections import defaultdict
# class Solution:
#     def solveSudoku(self, board: [[str]]) -> None:
#         rows, cols, triples, visit = defaultdict(set), defaultdict(set), defaultdict(set), []
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] != ".":
#                     rows[r].add(board[r][c])
#                     cols[c].add(board[r][c])
#                     triples[(r // 3, c // 3)].add(board[r][c])
#                 else:
#                     visit.append((r, c))
#         def dfs():
#             if not visit:
#                 return True
#             r, c = visit.pop()
#             t = (r // 3, c // 3)
#             for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
#                 if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
#                     board[r][c] = dig
#                     rows[r].add(dig)
#                     cols[c].add(dig)
#                     triples[t].add(dig)
#                     # visit.pop()
#                     if dfs():
#                         return True
#                     else:
#                         board[r][c] = "."
#                         rows[r].discard(dig)
#                         cols[c].discard(dig)
#                         triples[t].discard(dig)
#                         # visit.append((r, c))
#             visit.append((r, c))
#             return False
#         dfs()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

pprint.pprint(board)
sol = Solution()
sol.solveSudoku(board)
pprint.pprint(board)
print(board == Output)
