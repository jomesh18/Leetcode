'''
1260. Shift 2D Grid
Easy

836

219

Add to List

Share
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
Accepted
51,074
Submissions
77,533
Seen this question in a real interview before?

Yes

No

'''
#using reverse
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        arr = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                arr[n*i+j] = grid[i][j]
        def reverse(arr, i,j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        k %= (m*n)
        reverse(arr, 0, m*n-1)
        reverse(arr, 0, k-1)
        reverse(arr, k, m*n-1)
        
        for i in range(m*n):
            grid[i//n][i%n] = arr[i]
            
        return grid

#using list slicing
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        arr = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                arr[n*i+j] = grid[i][j]

        k %= (m*n)
        arr = arr[-k:] + arr[:-k]
        
        for i in range(m*n):
            grid[i//n][i%n] = arr[i]
            
        return grid

#O(1) space
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= (m*n)
        def reverse(i, j):
            while i < j:
                r1, c1, r2, c2 = i//n, i % n, j //n, j%n
                grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]
                i += 1
                j -= 1
        reverse(0, m*n-1)
        reverse(0, k-1)
        reverse(k, m*n-1)
        
        return grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        ans = []
        
        start = m*n-(k%(m*n))
        
        for i in range(start, start + m*n):
            j = i %(m*n)
            
            r, c = j // n, j % n
            
            if not (i-start)%n:
                ans.append([])
            ans[-1].append(grid[r][c])
            
        return ans