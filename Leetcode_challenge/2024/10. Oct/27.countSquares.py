'''
1277. Count Square Submatrices with All Ones
Medium

5334

97

Add to List

Share
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        one_sums = [[0]*n for _ in range(m)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                one_sums[i][j] = (one_sums[i][j+1] if j+1 < n else 0) + (one_sums[i+1][j] if i+1 < m else 0) - (one_sums[i+1][j+1] if (i+1 < m and j+1 < n) else 0)
                if matrix[i][j] == 1:
                    one_sums[i][j] += 1
        ans = 0
        for l in range(1, min(m, n)+1):
            sq = l * l
            for i in range(m-l+1):
                for j in range(n-l+1):
                    curr = one_sums[i][j] - (one_sums[i+l][j] if i+l < m else 0) - (one_sums[i][j+l] if j+l < n else 0) + (one_sums[i+l][j+l] if (i+l < m and j+l < n) else 0)
                    if curr == sq:
                        ans += 1
        return ans


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                    ans += dp[i+1][j+1]
        return ans