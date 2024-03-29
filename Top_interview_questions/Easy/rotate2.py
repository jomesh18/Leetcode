'''
Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:

Input: matrix = [[1]]
Output: [[1]]

Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

 

Constraints:

    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        lt, rt, rb, lb = (0, 0), (0, n-1), (n-1, n-1), (n-1, 0)
        k = n
        while k >= 2:
            for i in range(k-1):
                temp = matrix[lt[0]][lt[1]+i]
                matrix[lt[0]][lt[1]+i] = matrix[lb[0]-i][lb[1]]
                matrix[lb[0]-i][lb[1]] = matrix[rb[0]][rb[1]-i]
                matrix[rb[0]][rb[1]-i] = matrix[rt[0]+i][rt[1]]
                matrix[rt[0]+i][rt[1]] = temp
                # print(matrix)
            k -= 2
            lt = (lt[0]+1, lt[1]+1)
            rt = (rt[0]+1, rt[1]-1)
            rb = (rb[0]-1, rb[1]-1)
            lb = (lb[0]-1, lb[1]+1)

#transpose on main diagonal and reflect right to left
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def transpose(mat):
            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                    
        def reflect(mat):
            for i in range(n):
                for j in range(n//2):
                    mat[i][j], mat[i][-j-1] = mat[i][-j-1], mat[i][j]
            
        transpose(matrix)
        reflect(matrix)

#transpose on anti diagonal and reflect from top to bottom
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def transpose(mat):
            for i in range(n-1):
                for j in range(i+1, n):
                    mat[i][n-1-j], mat[j][n-1-i] = mat[j][n-1-i], mat[i][n-1-j]
                    
        def reflect(mat):
            for j in range(n):
                for i in range(n//2):
                    mat[i][j], mat[n-1-i][j] = mat[n-1-i][j], mat[i][j]
            
        transpose(matrix)
        print(matrix)
        reflect(matrix)
        print(matrix)
