'''
1329. Sort the Matrix Diagonally
Medium

2295

193

Add to List

Share
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
Example 2:

Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
Accepted
108,581
Submissions
131,225
'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        def collect_sort_replace(r, c):
            curr = []
            while r < m and c < n:
                curr.append(mat[r][c])
                r += 1
                c += 1
            curr.sort(reverse=True)
            r -= 1
            c -= 1
            for v in curr:
                mat[r][c] = v
                r -= 1
                c -= 1
                
        for c in range(n):
            collect_sort_replace(0, c)
        for r in range(1, m):
            collect_sort_replace(r, 0)
        
        return mat


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        d = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        
        for k in d:
            d[k].sort(reverse=True)
            
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop()
                
        return mat