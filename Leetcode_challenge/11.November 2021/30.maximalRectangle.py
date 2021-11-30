'''
85. Maximal Rectangle
Hard

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = []
Output: 0

Example 3:

Input: matrix = [["0"]]
Output: 0

Example 4:

Input: matrix = [["1"]]
Output: 1

Example 5:

Input: matrix = [["0","0"]]
Output: 0

 

Constraints:

    rows == matrix.length
    cols == matrix[i].length
    0 <= row, cols <= 200
    matrix[i][j] is '0' or '1'.

Accepted
263,864
Submissions
638,625
'''
class Solution:
    def maximalRectangle(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]: return 0

        cols = len(matrix[0])
        heights = [0] * (cols+1)
        ans = 0

        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            stack = [-1]
            for i in range(cols+1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h*w)
                stack.append(i)
        return ans

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6

# matrix = []
# Output: 0

# matrix = [["0"]]
# Output: 0

# matrix = [["1"]]
# Output: 1

# matrix = [["0","0"]]
# Output: 0

sol = Solution()
print(sol.maximalRectangle(matrix))
