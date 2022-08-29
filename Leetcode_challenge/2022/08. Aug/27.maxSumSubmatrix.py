'''
363. Max Sum of Rectangle No Larger Than K
Hard

3023

151

Add to List

Share
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

 

Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105
 

Follow up: What if the number of rows is much larger than the number of columns?
'''
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_sum = [[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                pre_sum[i][j] = matrix[i][j] + (pre_sum[i][j-1] if j > 0 else 0)
        max_ = float('-inf')
        for cs in range(n):
            for ce in range(cs, n):
                curr = 0
                seen = [0]
                for row in range(m):
                    curr += pre_sum[row][ce] - (pre_sum[row][cs-1] if cs > 0 else 0)
                    ind = bisect.bisect_left(seen, curr-k)
                    if ind < len(seen): max_ = max(max_, curr-seen[ind])
                    seen.append(curr)
                    seen.sort()
        return max_

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_sum = [[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                pre_sum[i][j] = matrix[i][j] + (pre_sum[i][j-1] if j > 0 else 0)
        max_ = float('-inf')
        for cs in range(n):
            for ce in range(cs, n):
                curr = 0
                seen = [0]
                for row in range(m):
                    curr += pre_sum[row][ce] - (pre_sum[row][cs-1] if cs > 0 else 0)
                    ind = bisect.bisect_left(seen, curr-k)
                    if ind < len(seen): max_ = max(max_, curr-seen[ind])
                    bisect.insort(seen, curr)
        return max_


#tle now
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_sum = [[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                pre_sum[i][j] = matrix[i][j] + (pre_sum[i][j-1] if j > 0 else 0)
        max_ = float('-inf')
        for cs in range(n):
            for ce in range(cs, n):
                curr = 0
                seen = SortedList([0])
                for row in range(m):
                    curr += pre_sum[row][ce] - (pre_sum[row][cs-1] if cs > 0 else 0)
                    ind = seen.bisect_left(curr-k)
                    if ind < len(seen): max_ = max(max_, curr-seen[ind])
                    seen.add(curr)
        return max_


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_sum = [list(accumulate(row)) for row in matrix]
        ans = float('-inf')
        for cs in range(n):
            for ce in range(cs, n):
                s = 0
                seen = [0]
                for r in range(m):
                    s += pre_sum[r][ce] - (pre_sum[r][cs-1] if cs > 0 else 0)
                    ind = bisect.bisect_left(seen, s-k)
                    if ind < len(seen):
                        ans = max(ans, s-seen[ind])
                    bisect.insort(seen, s)
        return ans