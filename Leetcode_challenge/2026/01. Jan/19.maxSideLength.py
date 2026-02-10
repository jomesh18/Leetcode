'''
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:

Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than or equal to 4 is 2 as shown.

Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 300
    0 <= mat[i][j] <= 104
    0 <= threshold <= 105
'''
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        row_sums = [[0]*(n+1) for _ in range(m)]
        min_val = float('inf')
        for i in range(m):
            for j in range(n):
                row_sums[i][j+1] = row_sums[i][j] + mat[i][j]
                min_val = min(min_val, mat[i][j])
        max_l = min(m, n)
        if min_val > threshold:
            return 0
        def check(l):
            for r in range(m-l+1):
                for c in range(n-l+1):
                    s = 0
                    for i in range(l):
                        s += row_sums[r+i][c+l] - row_sums[r+i][c]
                    if s <= threshold: return True
            return False

        ans = 1
        lo, hi = 1, max_l+1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = max(ans, mid)
                lo = mid + 1
            else:
                hi = mid
        
        return ans
