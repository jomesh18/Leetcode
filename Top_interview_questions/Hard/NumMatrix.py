'''

817 · Range Sum Query 2D - Mutable
Algorithms
Medium
Accepted Rate
48%
Description
Solution14
Notes62
Discuss3
Leaderboard
Record

Description
Given a 2D matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2). And the elements of the matrix could be changed.

You have to implement three functions:

NumMatrix(matrix) The constructor.
sumRegion(row1, col1, row2, col2) Return the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
update(row, col, val) Update the element at (row, col) to val.
The matrix is only modifiable by update.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
Example
Example 1:

Input:
  NumMatrix(
    [[3,0,1,4,2],
     [5,6,3,2,1],
     [1,2,0,1,5],
     [4,1,0,1,7],
     [1,0,3,0,5]]
  )
  sumRegion(2,1,4,3)
  update(3,2,2)
  sumRegion(2,1,4,3)
Output:
  8
  10
Example 2:

Input:
  NumMatrix([[1]])
  sumRegion(0, 0, 0, 0)
  update(0, 0, -1)
  sumRegion(0, 0, 0, 0)
Output:
  1
  -1
'''
class BIT:
    def __init__(self, n):
        self.bit = [0]*(n+1)

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i = self.get_parent(i)
        return s

    def update(self, i, delta):
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i = self.get_next(i)

    def get_next(self, i):
        return i + (i & -i)

    def get_parent(self, i):
        return i - (i & -i)

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self.bit = BIT(self.m*self.n)
        for i in range(self.m):
            for j in range(self.n):
                pos = i*(self.n)+j
                val = self.matrix[i][j]
                self.bit.update(pos, val)
                print('inside init', i, j, self.bit.bit)
        print('final', self.bit.bit)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        i = (row+1)*(self.n+1) + col + 1
        delta = -self.matrix[row][col] + val
        self.matrix[row][col] = val
        self.bit.update(i, delta)
        print('updated', row, col, val, self.bit.bit)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        a = self.bit.sum((row2+1)*(self.n+1)+col2+1)
        b = self.bit.sum((row2+1)*(self.n+1)+col1)
        c = self.bit.sum(row1*(self.n+1)+col2+1)
        d = self.bit.sum(row1*(self.n+1)+col1)
        ans = a-b-c+d
        print('inside sum', a, b, c, d, ans)
        return ans

# Your NumMatrix object will be instantiated and called as such:
matrix = [[1,2,3], [2,1,0]]
obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)