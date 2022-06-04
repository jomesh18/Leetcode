'''
51. N-Queens
Hard

6270

156

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
Accepted
383,785
Submissions
654,957
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        
        self.res = []
        
        def backtrack(i, board):
            if i == n:
                self.res.append(["".join(l) for l in board])
                return
            for j in range(n):
                if is_feasible(i, j, board):
                    board[i][j] = 'Q'
                    backtrack(i+1, board)
                    board[i][j] = '.'
                    
        def is_feasible(i, j, board):
            #checking column
            for k in range(n):
                if k != i and board[k][j] == 'Q':
                    return False
            #checking row, no need for this because we dont place Q in the same row
            for k in range(n):
                if k != j and board[i][k] == 'Q':
                    return False
            #checking main diagonal
            diff = min(i, j)
            start, end = i-diff, j-diff
            while start < n and end < n:
                if (start, end) != (i, j) and board[start][end] == 'Q':
                    return False
                start += 1
                end += 1
            #checking antidiagonal
            s = i+j
            k = 0
            while k < n:
                if 0<=k<n and 0<=s-k<n and board[k][s-k] == 'Q':
                    return False
                k += 1
            return True

        backtrack(0, board)
        return self.res

#better than first
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        
        self.res = []
        
        def backtrack(i, board):
            if i == n:
                self.res.append(["".join(l) for l in board])
                return
            for j in range(n):
                if is_feasible(i, j, board):
                    board[i][j] = 'Q'
                    backtrack(i+1, board)
                    board[i][j] = '.'
                    
        def is_feasible(i, j, board):
            #checking column
            for k in range(i):
                if board[k][j] == 'Q':
                    return False

            #checking main diagonal
            k, l = i-1, j-1
            while k>=0 and l >=0:
                if board[k][l] == 'Q':
                    return False
                k -= 1
                l -= 1
            #checking antidiagonal
            k, l = i-1, j+1
            while k >= 0 and l < n:
                if board[k][l] == 'Q':
                    return False
                k -= 1
                l += 1
            return True

        backtrack(0, board)
        return self.res

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(queens, xy_su, xy_diff):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and p+q not in xy_su and p-q not in xy_diff:
                    print(xy_su, xy_diff)
                    backtrack(queens+[q], xy_su+[p+q], xy_diff+[p-q])
        
        res = []
        backtrack([], [], [])
        return  [['.'*i+'Q'+'.'*(n-i-1) for i in sol] for sol in res]