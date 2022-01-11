'''
Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:

Input: matrix = [[-5]], k = 1
Output: -5

 

Constraints:

    n == matrix.length
    n == matrix[i].length
    1 <= n <= 300
    -109 <= matrix[i][j] <= 109
    All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    1 <= k <= n2

'''

class Solution:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        n, beg, end = len(matrix), matrix[0][0], matrix[-1][-1]
        def check(m):
            i, j, cnt = 0, n-1, 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > m: j -= 1
                cnt += (j + 1)
            return cnt
        while beg < end:
            mid = (beg + end)//2
            if check(mid) < k:
                beg = mid + 1
            else:
                end = mid
        return beg

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
# Output: 13

matrix = [[-5]]
k = 1
# Output: -5

s = Solution()
print(s.kthSmallest(matrix, k))
