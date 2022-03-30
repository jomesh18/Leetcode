'''
74. Search a 2D Matrix
Medium

6639

254

Add to List

Share
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
Accepted
704,733
Submissions
1,628,864
Seen this question in a real interview before?

Yes

No

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        lo, hi = 0, r*c
        while lo < hi:
            mid = lo + ((hi-lo)>>1)
            # print(lo, hi, mid, mid//c, mid%c)
            if matrix[mid//c][mid%c] >= target:
                hi = mid
            else:
                lo = mid + 1
        return True if (lo < r*c and matrix[lo//c][lo%c] == target) else False