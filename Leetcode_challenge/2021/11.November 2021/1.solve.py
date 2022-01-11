'''
130. Surrounded Regions
Medium

3770

939

Add to List

Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
Accepted
348,345
Submissions
1,089,492
'''
class Solution:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j, this_visit):
            if i == 0 or j == 0 or i == m-1 or j == n-1:
                self.in_boundary = True
            this_visit.add((i, j))
            for u, v in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0<=u<m and 0<=v<n and (u, v) not in this_visit and board[u][v] == "O":
                    dfs(u, v, this_visit)
            
        m, n = len(board), len(board[0])
        visited = set()
        self.in_boundary = False
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == "O":
                    self.in_boundary = False
                    this_visit = set()
                    dfs(i, j, this_visit)
                    # print(self.in_boundary)
                    if not self.in_boundary:
                        for k, l in this_visit:
                            board[k][l] = "X"
                    visited.update(this_visit)

#from leetcode
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rlen = len(board)
        clen = len(board[0])
        
        # find borders
        borders = []
        for i in range(rlen):
            for j in [0, clen - 1]:
                borders.append((i, j))
        
        for i in [0, rlen - 1]:
            for j in range(clen):
                borders.append((i, j))
        
        # mark "escaped" cells with 'E'
        direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i, j in borders:
            if board[i][j] == 'O':
                to_visit = [(i, j)]
                while to_visit:
                    curr_i, curr_j = to_visit.pop(0)      
                    board[curr_i][curr_j] = 'E'
                    for diff_r, diff_c in direct:
                        r, c = curr_i + diff_r, curr_j + diff_c
                        if 0 <= r < rlen and 0 <= c < clen and board[r][c] == 'O':
                            board[r][c] = 'E'
                            to_visit.append((r, c))

        for i in range(rlen):
            for j in range(clen):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

board = [["X"]]
# Output: [["X"]]

sol = Solution()
print(board)
sol.solve(board)
print(board)
