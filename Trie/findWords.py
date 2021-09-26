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
#taking too much time, 8000ms
# class TrieNode:
#     def __init__(self):
#         self.neighbors = {}
#         self.isWord = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word):
#         current = self.root
#         for w in word:
#             current = current.neighbors.setdefault(w, TrieNode())
#         current.isWord = True

# class Solution:
#     def findWords(self, board: [[str]], words: [str]) -> [str]:
#         trie = Trie()
#         res = []
#         node = trie.root
#         for word in words:
#             trie.addWord(word)
#         # print(print_trie(trie))
#         for p in range(len(board)):
#             for q in range(len(board[0])):
#                 self.dfs(node, p, q, board, res, "")
#         return res

#     def dfs(self, node, i, j, board, res, path):
#         if node.isWord:
#             res.append(path)
#             # node.isWord = False
#         if i<0 or i>=len(board) or j<0 or j>=len(board[0]): return
#         temp = board[i][j]
#         if temp not in node.neighbors: return
#         node = node.neighbors[temp]
#         board[i][j] = "#"
#         for k, l in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
#             self.dfs(node, i+k, j+l, board, res, path+temp)
#         board[i][j] = temp
#         return res

#from leetcode fastest, <100ms
class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        # parse character and build a set 
        charSet = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                charSet.add(board[i][j])
        # build a trie
        root = {}
        stop = '$'
        for word in words:
            skip = False
            for ch in word:
                if ch not in charSet:
                    skip = True
                    break
            if skip: # next word
                continue
            
            node = root
            for ch in word:
                node = node.setdefault(ch, {}) 
            node[stop] = stop
                
        res = []
        searched = set()
        
        def dfs(i, j, node, string):
            if stop in node: # find a match word
                res.append(string)
                node.pop(stop, None) # avoid re-compute
            if (i, j, string) in searched:
                return
            searched.add((i, j, string))
            
            temp , board[i][j] = board[i][j], '#' # prevent for revisiting
            
            for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in node:
                    dfs(nx, ny, node[board[nx][ny]], string + board[nx][ny])
                    if not node[board[nx][ny]]:
                        node.pop(board[nx][ny], None)
            board[i][j] = temp
            return
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    node = root
                    dfs(i, j, node[board[i][j]], board[i][j])
        return res

def print_trie(trie):
    node = trie.root
    res = []
    def dfs(node, res, temp):
        if node.isWord:
            res.append(temp)
        for n in node.neighbors:
            dfs(node.neighbors[n], res, temp+n)

    dfs(node, res, "")
    return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
# # Output: ["eat","oath"]

# board = [["a","b"],["c","d"]]
# words = ["abcb"]
# # # # # Output: []

# board = [["a","b"],["c","d"]]
# words = ["abd", "acd", "abcb"]
# # # # # Output: ["abd", "acd"]

sol = Solution()
print(sol.findWords(board, words))
