'''
688. Knight Probability in Chessboard
Medium

3110

400

Add to List

Share
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

 

Example 1:

Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
Example 2:

Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000
 

Constraints:

1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n - 1
'''
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(1, -2), (-1, -2), (2, -1), (-2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]
        memo = [[[-1]*(k+1) for _ in range(n)] for _ in range(n)]
        def dfs(i, j, c):
            if not c: return 1
            if memo[i][j][c] != -1: return memo[i][j][c]
            memo[i][j][c] = 0
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<n:
                    memo[i][j][c] += dfs(ni, nj, c-1)
            return memo[i][j][c]
        return dfs(row, column, k)/(8**k)
