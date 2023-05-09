'''
54. Spiral Matrix
Medium

11451

1049

Add to List

Share
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lr, lc, hr, hc = 0, 0, len(matrix)-1, len(matrix[0])-1
        
        ans = []
        r, c = 0, 0
        while lr <= hr and lc <= hc:
            for k in range(lc, hc+1):
                ans.append(matrix[lr][k])
            for k in range(lr+1, hr+1):
                ans.append(matrix[k][hc])
            if lr != hr:
                for k in range(hc-1, lc-1, -1):
                    ans.append(matrix[hr][k])
            if lc != hc:
                for k in range(hr-1, lr, -1):
                    ans.append(matrix[k][lc])
            
            lr += 1
            lc += 1
            hr -= 1
            hc -= 1
        return ans