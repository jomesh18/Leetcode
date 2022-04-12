'''
289. Game of Life
Medium

4068

410

Add to List

Share
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
Accepted
307,599
Submissions
483,687
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        next_live, next_dead = set(), set()
        neighbors = {(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)}
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                for u, v in neighbors:
                    if 0<=i+u<m and 0<=j+v<n:
                        if board[i+u][j+v] == 1: live += 1
                if board[i][j]:
                    if live < 2 or live > 3: next_dead.add((i, j))
                    elif 2<=live<=3: next_live.add((i, j))
                elif live == 3: next_live.add((i, j))
        for i, j in next_live:
            board[i][j] = 1
        for i, j in next_dead:
            board[i][j] = 0

#O(1) space using two bits      
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def count_live(i, j):
            count = -(board[i][j] & 1)
            for a in range(max(i-1, 0), min(i+1, m-1)+1):
                for b in range(max(j-1, 0), min(j+1, n-1)+1):
                    count += board[a][b] & 1
            return count
                    
        for i in range(m):
            for j in range(n):
                live = count_live(i, j)
                if board[i][j] and live >= 2 and live <= 3:
                    board[i][j] = 3
                elif not board[i][j] and live == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        