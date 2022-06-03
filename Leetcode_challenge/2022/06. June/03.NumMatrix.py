'''
304. Range Sum Query 2D - Immutable
Medium

2600

250

Add to List

Share
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
Accepted
228,158
Submissions
474,911
'''
# O(m)*queries
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [list(accumulate(row)) for row in matrix]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for row in range(row1, row2+1):
            s += self.presum[row][col2]-(self.presum[row][col1-1] if col1>0 else 0)
        return s

# O(1)*queries
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i>0 and j > 0:
                    self.dp[i][j] = self.dp[i][j-1]+self.dp[i-1][j]-self.dp[i-1][j-1]+matrix[i][j]
                elif i == 0 and j >0:
                    self.dp[i][j] = self.dp[i][j-1]+matrix[i][j]
                elif j == 0 and i > 0:
                    self.dp[i][j] = self.dp[i-1][j]+matrix[i][j]
                elif i == 0 and j == 0:
                    self.dp[i][j] = matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2][col2] - (self.dp[row1-1][col2] if row1>0 else 0)  - (self.dp[row2][col1-1] if col1 >0 else 0) + (self.dp[row1-1][col1-1] if (row1>0 and col1>0) else 0)
        # elif row1 == 0 and col1 > 0:
        #     return dp[row2][col2] - dp[row2][col1-1]
        # elif row1 > 0 and col1 == 0:
        #     return dp[row2][col2] - dp[row1-1][col2]
        # elif row1 == 0 and col1 == 0:
        #     return dp[row2][col1]
         
# O(1)*queries, cleaner implementation   
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.dp[i+1][j+1] = self.dp[i+1][j]+self.dp[i][j+1]-self.dp[i][j]+matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1]  - self.dp[row2+1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)