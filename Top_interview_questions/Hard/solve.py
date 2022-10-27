'''
130. Surrounded Regions
Medium

5997

1369

Add to List

Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        def dfs(i, j):
            for u, v in neighbors:
                new_x, new_y = i+u, j+v
                if 0<=new_x<m and 0<=new_y<n and board[new_x][new_y] == 'O':
                    board[new_x][new_y] = 0
                    dfs(new_x, new_y)
            
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 0
                dfs(i, 0)
            if board[i][n-1] == 'O':
                board[i][n-1] = 0
                dfs(i, n-1)
        for i in range(n):
            if board[0][i] == 'O':
                board[0][i] = 0
                dfs(0, i)
            if board[m-1][i] == 'O':
                board[m-1][i] = 0
                dfs(m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] = "O"            
                    