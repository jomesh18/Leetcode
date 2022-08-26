'''
Word Search

Solution
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
            if k == len(word):
                return True
            for u, v in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0<=u<m and 0<=v<n and (u, v) not in visited and board[u][v] == word[k]:
                    visited.add((u, v))
                    if dfs(u, v, visited, k+1):
                        return True
                    visited.remove((u, v))
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, {(i, j)}, 1):
                        return True
        return False

#fastest on leetcode, simple tricks to speed up
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(row, col, i=0):
            if len(word) == i:
                return True

            if not 0 <= row < rows or not 0 <= col < cols or board[row][col] != word[i]:
                return False

            temp = board[row][col]
            board[row][col] = None
            found = (
                search(row - 1, col, i + 1)
                or search(row, col + 1, i + 1)
                or search(row + 1, col, i + 1)
                or search(row, col - 1, i + 1)
            )
            board[row][col] = temp
            return found

        rows = len(board)
        cols = len(board[0])
        word_dict = Counter(word)
        board_dict = Counter(chain.from_iterable(board))

        if any(count > board_dict[char] for char, count in word_dict.items()):
            return False

        if word_dict[word[0]] > word_dict[word[-1]]:
            word = word[::-1]

        return any(search(row, col) for row in range(rows) for col in range(cols))
        