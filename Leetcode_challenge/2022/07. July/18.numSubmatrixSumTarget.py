'''
1074. Number of Submatrices That Sum to Target
Hard

2711

61

Add to List

Share
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0
 

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
'''
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        #prefix sum of rows
        for r in range(m):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c-1]
        res = 0
        for cs in range(n):
            for ce in range(cs, n):
                s = 0
                mp = {0: 1}
                for r in range(m):
                    s += matrix[r][ce] - (matrix[r][cs-1] if cs else 0)
                    res += mp.get(s-target, 0)
                    mp[s] = mp.get(s, 0) + 1
        return res
            