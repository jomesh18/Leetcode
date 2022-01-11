'''
Range Addition II

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

 

Example 1:

Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4

Example 3:

Input: m = 3, n = 3, ops = []
Output: 9

 

Constraints:

    1 <= m, n <= 4 * 104
    1 <= ops.length <= 104
    ops[i].length == 2
    1 <= ai <= m
    1 <= bi <= n

'''
# memory limit exceeded
# from collections import defaultdict
# class Solution:
#     def maxCount(self, m: int, n: int, ops: [[int]]) -> int:
#         d = defaultdict(int)
#         for i, j in ops:
#             for u in range(i):
#                 for v in range(j):
#                     d[(u, v)] += 1
#         c = 0
#         max_val = max([0] + list(d.values()))
#         if max_val == 0:
#             return m*n
#         for v in d.values():
#             if v == max_val:
#                 c += 1
#         return c

#tle
# class Solution:
#     def maxCount(self, m: int, n: int, ops: [[int]]) -> int:
#         mat = [[0 for _ in range(n)] for _ in range(m)]
#         # print(mat)
#         for i, j in ops:
#             for u in range(i):
#                 for v in range(j):
#                     mat[u][v] += 1
#         count = 0
#         max_val = 0
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] == max_val:
#                     count += 1
#                 elif mat[i][j] > max_val:
#                     max_val = mat[i][j]
#                     count = 1
#         return count

#from leetcode
class Solution:
    def maxCount(self, m: int, n: int, ops: [[int]]) -> int:
        xmin = m
        ymin = n
        for i in ops:
            if i[0] < xmin:
                xmin=i[0]
            if i[1] < ymin:
                ymin=i[1]
        return xmin*ymin

m = 3
n = 3
ops = [[2,2],[3,3]]
# Output: 4

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# # Output: 4

m = 3
n = 3
ops = []
# # Output: 9

m = 2
n = 3
ops = []
#Output: 

m = 39999
n = 39999
ops = [[19999,19999]]
# #Output: 

sol = Solution()
print(sol.maxCount(m, n, ops))
