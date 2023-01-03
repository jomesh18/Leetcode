'''
https://www.lintcode.com/problem/817/
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

'''
# better naming,

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.bit = [[0 for _ in range(self.cols + 1)] for _ in range(self.rows + 1)]
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r, c, matrix[r][c])
        
    def lowbit(self, x):
        return x & (-x)
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        r = row + 1
        while r <= self.rows:
            c = col + 1
            while c <= self.cols:
                self.bit[r][c] += delta
                c += self.lowbit(c)
            r += self.lowbit(r)
    def getPrefixSum(self, row, col):
        r = row + 1
        sum = 0
        while r > 0:
            c = col + 1
            while c > 0:
                sum += self.bit[r][c]
                c -= self.lowbit(c)
            r -= self.lowbit(r)
        return sum
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = self.getPrefixSum(row2, col2)
        sum_upside = self.getPrefixSum(row1 - 1, col2)
        sum_leftside = self.getPrefixSum(row2, col1 - 1)
        sum_small = self.getPrefixSum(row1 - 1, col1 - 1)
        return sum - sum_upside - sum_leftside + sum_small
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10

test = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
r = test.getPrefixSum(1, 1)
print(r)
r = test.getPrefixSum(2, 2)
print(r)
r = test.sumRegion(2, 1, 4, 3)
print(r)
print(test.matrix)
print(test.bit)
test.update(3, 2, 2)
print(test.matrix)
print(test.bit)
r = test.sumRegion(2, 1, 4, 3)
print(r)
'''

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0]*self.n for _ in range(self.m)]
        self.bit = [[0]*(self.n+1) for _ in range(self.m+1)]
        for r in range(self.m):
            for c in range(self.n):
                self.update(r, c, matrix[r][c])
        print(self.bit)
        print(self.matrix)

    def lowbit(self, a):
        return a & (-a)

    def get_sum(self, row, col):
        r = row + 1
        s = 0
        while r > 0:
            c = col + 1
            while c > 0:
                s += self.bit[r][c]
                c -= self.lowbit(c)
            r -= self.lowbit(r)
        return s

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        r = row + 1
        while r <= self.m:
            c = col + 1
            while c <= self.n:
                self.bit[r][c] += delta
                c += self.lowbit(c)
            r += self.lowbit(r)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        tot = self.get_sum(row2, col2)
        top_left = self.get_sum(row1-1, col1-1)
        left = self.get_sum(row2, col1-1)
        top = self.get_sum(row1-1, col2)
        return tot - left - top + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)