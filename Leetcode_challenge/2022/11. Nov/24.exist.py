'''
79. Word Search
Medium

11590

465

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
        
        def dfs(i, j, visited, k):
            if k == len(word): return True
            for ni, nj in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)):
                if 0<=ni<m and 0<=nj<n and board[ni][nj] == word[k] and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    if dfs(ni, nj, visited, k+1):
                        return True
                    visited.remove((ni, nj))
            return False
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, {(i, j)}, 1): return True
        return False