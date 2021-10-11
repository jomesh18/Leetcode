'''
212. Word Search II
Hard

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
from collections import Counter
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["#"] = "#"

class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        def dfs(node, board, i, j, temp):
            if node.get("#"):
                node.pop("#")
                res.append(temp)
            # print(i, j, temp, searched)
            if (i, j, temp) in searched:
                return
            searched.add((i, j, temp))
            t, board[i][j] = board[i][j], "$"
            for k, l in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0<=k<m and 0<=l<n and board[k][l] in node:
                    dfs(node[board[k][l]], board, k, l, temp+board[k][l])
                    if not node[board[k][l]]:
                        node.pop(board[k][l])
            board[i][j] = t
        searched = set()
        trie = Trie()
        count = Counter()
        for row in board:
            count += Counter(row)
        for word in words:
            coun = Counter(word)
            skip = False
            for key in coun:
                if coun[key] > count[key]:
                    skip = True
            if not skip:
                trie.insert(word)
        node = trie.root
        res = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in node:
                    dfs(node[char], board, i, j, char)
        return res

# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# # Output: ["eat","oath"]

# board = [["a","b"],["c","d"]]
# words = ["abcb"]
# # # Output: []

# board = [["o","a","a","o"],["e","t","a","a"],["i","a","k","t"],["i","f","l","h"]]
# words = ["oath","pea","eat","rain"]

board = [["a","b","c","e"],["z","z","d","z"],["z","z","c","z"],["z","a","b","z"]]
words = ["abcdce"]

sol = Solution()
print(sol.findWords(board, words))
