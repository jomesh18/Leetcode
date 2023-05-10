'''
59. Spiral Matrix II
Medium

5171

219

Add to List

Share
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        
        lr, hr, lc, hc = 0, n-1, 0, n-1
        i = 1
        while lr <= hr and lc <= hc:
            for c in range(lc, hc+1):
                ans[lr][c] = i
                i += 1
            for r in range(lr+1, hr+1):
                ans[r][hc] = i
                i += 1
            if lr != hr:
                for c in range(hc-1, lc-1, -1):
                    ans[hr][c] = i
                    i += 1
            if lc != hc:
                for r in range(hr-1, lr, -1):
                    ans[r][lc] = i
                    i += 1
            lr += 1
            lc += 1
            hc -= 1
            hr -= 1
            
        return ans


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            ans[i][j] = k+1
            if ans[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return ans