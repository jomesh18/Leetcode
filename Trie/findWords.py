'''
Word Search II

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
class TrieNode:
    def __init__(self):
        self.neighbors = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root
        for w in word:
            current = current.neighbors.setdefault(w, TrieNode())
        current.isWord = True

class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                node = trie.root
                res.append(self.dfs(node, i, j, board, ""))
        return res

    def dfs(self, node, i, j, board, path):
        if node.isWord: return path
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]): return
        temp = board[i][j]
        if temp not in node.neighbors: return
        node = node.neighbors[temp]
        board[i][j] = "#"
        for k, l in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            self.dfs(node, i+k, j+l, board, path+temp)
        board[i][j] = temp
            
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
# # Output: ["eat","oath"]

# board = [["a","b"],["c","d"]]
# words = ["abcb"]
# # Output: []

sol = Solution()
print(sol.findWords(board, words))
