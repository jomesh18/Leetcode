'''
Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
   Show Hint #1  
   Show Hint #2  
   Show Hint #3  
'''
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        res = []
        row_start, row_end, col_start, col_end = 0, len(matrix)-1, 0, len(matrix[0])-1
        while row_start < row_end and col_start < col_end:
            i, j = row_start, col_start
            while j <= col_end:
                res.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            while i <= row_end:
                res.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            while j >= col_start:
                res.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            while i > row_start:
                res.append(matrix[i][j])
                i -= 1
            row_start += 1
            col_start += 1
            row_end -= 1
            col_end -= 1
        if row_start == row_end and col_start < col_end:
            i, j = row_start, col_start
            while j <= col_end:
                res.append(matrix[i][j])
                j += 1
        elif row_start < row_end and col_start == col_end:
            i, j = row_start, col_start
            while i <= row_end:
                res.append(matrix[i][j])
                i += 1
        elif row_start == row_end and col_start == col_end:
            res.append(matrix[row_start][col_start])
        return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # Output: [1,2,3,6,9,8,7,4,5]

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# matrix = [[1,2],[3,4]]
# Output: [1,2,4,3]

sol = Solution()
print(sol.spiralOrder(matrix))
