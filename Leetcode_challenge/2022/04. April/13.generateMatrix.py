'''
59. Spiral Matrix II
Medium

3102

171

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
Accepted
331,160
Submissions
522,577
'''
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        mat = [[0]*n for _ in range(n)]
        s_r, s_c, e_r, e_c = 0, 0, n-1, n-1
        prev = 0
        #populating first row
        while s_r < e_r and s_c < e_c:
            for i in range(s_c, e_c+1):
                prev += 1
                mat[s_r][i] = prev
            for i in range(s_r+1, e_r+1):
                prev += 1
                mat[i][e_c] = prev
            for i in range(e_c-1, s_c-1, -1):
                prev += 1
                mat[e_r][i] = prev
            for i in range(e_r-1, s_r, -1):
                prev += 1
                mat[i][s_c] = prev


            s_r += 1
            s_c += 1
            e_r -= 1
            e_c -= 1
        if s_r == e_r == s_c == e_c:
            prev += 1
            mat[s_r][s_c] = prev

        return mat

#using layer
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        cnt = 1
        for layer in range((n+1)//2):
            
            for i in range(layer, n-layer):
                mat[layer][i] = cnt
                cnt += 1
            print(mat)
            for i in range(layer+1, n-layer):
                mat[i][n-1-layer] = cnt
                cnt += 1
            print(mat)
            for i in range(n-2-layer, layer-1, -1):
                mat[n-1-layer][i] = cnt
                cnt += 1
            print(mat)
            for i in range(n-2-layer, layer, -1):
                mat[i][layer] = cnt
                cnt += 1
            print(mat)
        return mat


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i, j, di, dj = 0, 0, 0, 1
        mat = [[0]*n for _ in range(n)]
        for val in range(n*n):
            mat[i][j] = val+1
            if mat[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return mat