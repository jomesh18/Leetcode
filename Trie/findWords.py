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
# import pprint
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
        # pprint.pprint(root)
        res = []
        searched = set()
        # searched = {}
        
        def dfs(i, j, node, string):
            if stop in node: # find a match word
                res.append(string)
                node.pop(stop, None) # avoid re-compute
            if (i, j, string) in searched:
                return
            searched[(i, j, string)] = searched.setdefault((i, j, string), 0) + 1
            
            temp , board[i][j] = board[i][j], '#' # prevent for revisiting
            
            for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in node:
                    dfs(nx, ny, node[board[nx][ny]], string + board[nx][ny])
                    if not node[board[nx][ny]]:
                        print("before {}".format(root))
                        node.pop(board[nx][ny], None)
                        print("after {}".format(root))
            board[i][j] = temp
            return
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    node = root
                    dfs(i, j, node[board[i][j]], board[i][j])
        return res



# #from leetcode
# from collections import Counter
# class Solution:
#     def findWords(self, board, words):
#         #make trie
#         count = Counter()
#         for l in board:
#             count += Counter(l)
#         trie={}
#         for w in words:
#             wc = Counter(w)
#             skip = False
#             for c in wc:
#                 # optimization, ignore word if there isn't enough c in board
#                 if wc[c] > count[c]:
#                     skip = True
#                     break
#             if skip:
#                 continue
#             t=trie
#             for c in w:
#                 if c not in t:
#                     t[c]={}
#                 t=t[c]
#             t['#']='#'
#         self.res=[]
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.find(board,i,j,trie,[])
#         return self.res
    
#     def find(self,board,i,j,trie,pre):
#         if '#' in trie:
#             # optimization, delete for avoiding duplicated matches
#             del trie["#"]
#             self.res.append(''.join(pre))
#         if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
#             return
#         if board[i][j] in trie:
#             tmp = board[i][j]
#             board[i][j] = '$'
#             pre.append(tmp)
#             self.find(board,i+1,j,trie[tmp],pre)
#             self.find(board,i,j+1,trie[tmp],pre)
#             self.find(board,i-1,j,trie[tmp],pre)
#             self.find(board,i,j-1,trie[tmp],pre)
#             board[i][j] = tmp
#             pre.pop()
#             if not trie[board[i][j]]:
#                 # nothing in trie[board[i][j]] because of matched before, delete node for optimization
#                 del trie[board[i][j]]



#from leetcode, stefan pochman, using complex numbers
# class Solution:
#     def findWords(self, board, words):

#         root = {}
#         for word in words:
#             node = root
#             for c in word:
#                 node = node.setdefault(c, {})
#             node[None] = True
#         board = {i + 1j*j: c
#                  for i, row in enumerate(board)
#                  for j, c in enumerate(row)}

#         found = []
#         def search(node, z, word):
#             if node.pop(None, None):
#                 found.append(word)
#             c = board.get(z)
#             if c in node:
#                 board[z] = None
#                 for k in range(4):
#                     search(node[c], z + 1j**k, word + c)
#                 board[z] = c
#         for z in board:
#             search(root, z, '')

#         return found


#leetcode, fastest my try
# import pprint
# from collections import Counter
# class Solution:
#     def findWords(self, board, words):
#         root = {}
#         count = Counter()
#         for c in board:
#             count += Counter(c)
#         for word in words:
#             wc = Counter(word)
#             #inserting words to trie
#             for c in word:
#                 skip = False
#                 if wc[c] > count[c]:
#                     skip = True
#                     break
#             if skip:
#                     continue # skip word
#             node = root
#             for c in word:
#                 node = node.setdefault(c, {})
#             node[None] = True
#         # pprint.pprint(root)
#         # print(print_trie(root))
#         def dfs(board, node, i, j, temp_r):
#             # print(board, node, i, j, temp_r)
#             if node.pop(None, None):
#                 res.append("".join(temp_r))
#             temp = board[i][j]
#             board[i][j] = "#"
#             for ix, iy in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
#                 if 0<=ix<len(board) and 0<=iy<len(board[0]) and board[ix][iy] in node:
#                     temp_r.append(board[ix][iy])
#                     dfs(board, node[board[ix][iy]], ix, iy, temp_r)
#                     if not node[board[ix][iy]]:
#                         node.pop(board[ix][iy], None)
#                     temp_r.pop()
#             board[i][j] = temp


#         res = []
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] in root:
#                     dfs(board, root[board[i][j]], i, j, [board[i][j]])
#         return res


# def print_trie(trie):
#     node = trie.root
#     res = []
#     def dfs(node, res, temp):
#         if node.isWord:
#             res.append(temp)
#         for n in node.neighbors:
#             dfs(node.neighbors[n], res, temp+n)

#     dfs(node, res, "")
#     return res

def print_trie(trie):
    node = trie
    res = []
    def dfs(node, res, temp):
        if node.get(None, None):
            node.pop(None)
            res.append(temp)
        for n in node:
            if n is None:
                dfs(node[n], res, temp)
            else:
                dfs(node[n], res, temp+n)

    dfs(node, res, "")
    return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
# # Output: ["eat","oath"]

# board = [["a","b"],["c","d"]]
# words = ["abcb"]
# # # # # # Output: []

# board = [["a","b"],["c","d"]]
# words = ["abd", "acd", "abcb"]
# # # # # # Output: ["abd", "acd"]

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain", "oathk"]

sol = Solution()
print(sol.findWords(board, words))
