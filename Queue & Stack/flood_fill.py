'''
Flood Fill

Solution
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''

#my try, note: no need for visited since we are changing colors as we visit
# from collections import deque
# class Solution:
#     def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
#         row = len(image)
#         column = len(image[0])
#         def bfs(sr, sc):
#             current_color = image[sr][sc]
#             neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
#             q = deque([(sr, sc)])
#             visited = [[False for _ in range(column)] for _ in range(row)]
#             while q:
#                 l = len(q)
#                 for _ in range(l):
#                     r, c = q.popleft()
#                     if not visited[r][c]:
#                         visited[r][c] = True
#                         image[r][c] = newColor
#                         for u, v in neighbors:
#                             if r+u>=0 and r+u<row and c+v>=0 and c+v<column and not visited[r+u][c+v] and image[r+u][c+v] == current_color:
#                                 q.append((r+u, c+v))
#         bfs(sr, sc)
#         return image

#my try using set
# from collections import deque
# class Solution:
#     def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
#         row = len(image)
#         column = len(image[0])
#         def bfs(sr, sc):
#             current_color = image[sr][sc]
#             neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
#             q = deque([(sr, sc)])
#             visited = set()
#             while q:
#                 l = len(q)
#                 for _ in range(l):
#                     r, c = q.popleft()
#                     if (r, c) not in visited:
#                         visited.add((r, c))
#                         image[r][c] = newColor
#                         for u, v in neighbors:
#                             if r+u>=0 and r+u<row and c+v>=0 and c+v<column and (r+u, c+v) not in visited and image[r+u][c+v] == current_color:
#                                 q.append((r+u, c+v))
#         bfs(sr, sc)
#         return image

#from leetcode solution, dfs

# class Solution(object):
#     def floodFill(self, image, sr, sc, newColor):
#         R, C = len(image), len(image[0])
#         color = image[sr][sc]
#         if color == newColor: return image
#         def dfs(r, c):
#             if image[r][c] == color:
#                 image[r][c] = newColor
#                 if r >= 1: dfs(r-1, c)
#                 if r+1 < R: dfs(r+1, c)
#                 if c >= 1: dfs(r, c-1)
#                 if c+1 < C: dfs(r, c+1)

#         dfs(sr, sc)
#         return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

s = Solution()
print(s.floodFill(image, sr, sc, newColor))
