'''
212. Word Search II
Hard

7235

312

Add to List

Share
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = {}
        for i, word in enumerate(words):
            curr = trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr['#'] = i
        
        def dfs(i, j, curr):
            if '#' in curr:
                ans.append(words[curr['#']])
                del curr['#']
            t, board[i][j] = board[i][j], '$'
            for ni, nj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0<=ni<m and 0<=nj<n and board[ni][nj] in curr:
                    dfs(ni, nj, curr[board[ni][nj]])
                    if not curr[board[ni][nj]]:
                        del curr[board[ni][nj]]
            board[i][j] = t
        
        ans = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]])
        return ans