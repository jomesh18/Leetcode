'''
1886. Determine Whether Matrix Can Be Obtained By Rotation
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
'''
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        equal = True
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    equal = False
                    break
        if equal: return True
        equal = True
        count= 0
        for j in range(n):
            for i in range(n-1, -1, -1):
                if mat[i][j] != target[count//n][count%n]:
                    equal = False
                    break
                count += 1
        if equal: return True
        equal = True
        count = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != target[count//n][count%n]:
                    equal = False
                    break
                count += 1
        if equal: return True
        equal = True
        count = 0
        for j in range(n-1, -1, -1):
            for i in range(n):
                if mat[i][j] != target[count//n][count%n]:
                    equal = False
                    break
                count += 1
        return equal