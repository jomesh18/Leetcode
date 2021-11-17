'''
62. Unique Paths
Medium

7056

267

Add to List

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
'''

#naive dfs, tle
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         self.count = 0
#         def dfs(i, j):
#             if (i, j) == (m-1, n-1):
#                 self.count += 1
#             for u, v in ((i, j+1), (i+1, j)):
#                 if 0<=u<m and 0<=v<n:
#                     dfs(u, v)
#         dfs(0, 0)
#         return self.count


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = {}
        def dfs(i, j, count):
            if (i, j) == (m-1, n-1):
                count += 1
                return count
            temp_count = 0
            for u, v in ((i, j+1), (i+1, j)):
                if 0<=u<m and 0<=v<n:
                    if (u, v) not in visited:
                        visited[(u, v)] = dfs(u, v, count)
                    temp_count += visited[(u, v)]
            return count+temp_count
        ans = dfs(0, 0, 0)
        # print(visited)
        return ans

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = {}
        self.count = 0
        def dfs(i, j):
            if (i, j) == (m-1, n-1):
                self.count += 1
                return True
            temp = False
            for u, v in ((i, j+1), (i+1, j)):
                if 0<=u<m and 0<=v<n:
                    if (u, v) not in visited:
                        visited[(u, v)] = dfs(u, v)
                        temp = visited[(u, v)] or temp
                    if visited[(u, v)]:    
                        self.count += 1
            return temp
                    
        dfs(0, 0)
        print(visited)
        return self.count