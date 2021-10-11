'''
Search a 2D Matrix II

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

 

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -109 <= matrix[i][j] <= 109
    All the integers in each row are sorted in ascending order.
    All the integers in each column are sorted in ascending order.
    -109 <= target <= 109

'''

# divide and conquer
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def search(left, right, up, down):
            if left>right or up>down:
                return False
            elif matrix[up][left] > target or matrix[down][right] < target:
                return False
            mid = left + ((right-left)>>2)
            row = up
            while row<=down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search(left, mid-1, row, down) or search(mid+1, right, up, row-1)

        return search(0, n-1, 0, m-1)


#from leetcode
# class Solution:
#     def searchMatrix(self, matrix: [[int]], target: int) -> bool:
#         j = -1
#         for row in matrix:
#             while j+len(row) and row[j] > target:
#                 j -= 1
#             if row[j] == target:
#                 return True
#         return False

matrix = [[-1,3]]
target = -1
# # Output: true

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
# # # # # Output: true

# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 20
# # # # # Output: false

# matrix = [[1,3,5]]
# target = 5
# # Output: True

sol = Solution()
print(sol.searchMatrix(matrix, target))
