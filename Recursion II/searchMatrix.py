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
# class Solution:
#     def searchMatrix(self, matrix: [[int]], target: int) -> bool:
#         print(matrix)
#         if not matrix or not matrix[0]: return False
#         m, n = len(matrix), len(matrix[0])
#         if m == 1 and n == 1:
#              return True if matrix[0][0] == target else False
#         column = n//2
#         row = 0
#         # print(m, n, column, matrix)
#         if matrix[0][column] >= target:
#             return self.searchMatrix([matrix[0][:column+1]], target)
#         if matrix[-1][column] < target:
#             return self.searchMatrix(matrix[:][column+1:], target)
#         for i in range(m):
#             if matrix[i][column] >= target:
#                 row = i
#                 break
#         if matrix[row][column] == target:
#             return True
#         upper_right_mat = [p[column+1:] for p in matrix[:row]]
#         lower_left_mat = [p[:column] for p in matrix[row:]]
        # return self.searchMatrix(upper_right_mat, target) or self.searchMatrix(lower_left_mat, target)

#naive divide and conquer, taking mid as pivot
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        def search(from_row, to_row, from_column, to_column):
            print(from_row, to_row, from_column, to_column)
            if 
            if from_row > to_row or from_column > to_column: return False
            if from_row == to_row and from_column == to_column: return target == matrix[from_row][from_column]
            i, j = from_row+(to_row-from_row)//2, from_column+(to_column-from_column)//2
            pivot = matrix[i][j]
            
            if pivot > target:
                return search(from_row, i-1, from_column, to_column) or search(i, to_row, j, to_column)
            elif pivot < target:
                return search(from_row, to_row, j+1, to_column) or search(i+1, to_row, from_column, j)
            else:
                return True

        return search(0, m-1, 0, n-1)


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
