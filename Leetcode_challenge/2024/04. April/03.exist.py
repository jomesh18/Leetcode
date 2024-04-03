'''
79. Word Search
Medium

15212

636

Add to List

Share
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, pos):
            if pos == len(word):
                return True
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and not visited[ni][nj] and board[ni][nj] == word[pos]:
                    visited[ni][nj] = True
                    if dfs(ni, nj, pos+1):
                        return True
                    visited[ni][nj] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[False]*n for _ in range(m)]
                    visited[i][j] = True
                    if dfs(i, j, 1): return True
        return False