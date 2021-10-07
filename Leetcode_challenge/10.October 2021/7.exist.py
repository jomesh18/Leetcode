'''
79. Word Search
Medium

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
#my try
# class Solution:
#     def exist(self, board: [[str]], word: str) -> bool:
#         def dfs(i, j, pos, board):
#             # print(pos)
#             self.count += 1
#             if pos == len(word): return True
#             temp, board[i][j] = board[i][j], "#"
#             for k, l in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
#                 # print(k, l, word[pos])
#                 if 0<=k<m and 0<=l<n and board[k][l] == word[pos]:
#                     if dfs(k, l, pos+1, board):
#                         # print("inside k {}, l {}, pos{}, board {}".format(k, l, pos, board))
#                         return True
#             board[i][j] = temp

#         m, n = len(board), len(board[0])
#         self.count = 0
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == word[0] and dfs(i, j, 1, board):
#                     print(self.count)
#                     return True
#         return False

#fastest, from leetcode
import pprint
from collections import defaultdict
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m, n, k = len(board), len(board[0]), len(word)
        hash = defaultdict(int)

        def dfs(i, j, letter):
            self.count += 1
            self.check.append((i, j, letter))
            # if hash[(i, j, letter)] > 1: 
            #     return False
            
            hash[(i, j, letter)] += 1
            if letter == k: 
                return True
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[letter]:
                board[i][j] = '#'
                for x, y in (i, j+1), (i, j-1), (i+1, j), (i-1, j):
                    if dfs(x, y, letter+1):
                        return True
                    
                board[i][j] = word[letter]
            return False
        self.check = []
        self.count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    print(len(hash), len(self.check))
                    # pprint.pprint(hash)
                    print(self.count)
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# Output: true

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
# # Output: true

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"], ["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
# Output: false

board = [["A","B","C","E", "F", "G"],["A","B","C","E", "F", "G"],["A","B","C","E", "F", "G"], ["A","B","C","E", "F", "G"],["B","C","C","E", "F", "G"],["A","D","E","E"]]
word = "ABCB"
# Output: false

sol = Solution()
print(sol.exist(board, word))
