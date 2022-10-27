'''
835. Image Overlap
Medium

546

168

Add to List

Share
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

 

Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0
 

Constraints:

n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
'''
# O(n**4), accepted, brute force
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        def shift_count(xshift, yshift, r, m):
            l_shift_count, r_shift_count = 0, 0
            for r_row, m_row in enumerate(range(yshift, n)):
                for r_col, m_col in enumerate(range(xshift, n)):
                    if m[m_row][m_col] == 1 and r[r_row][r_col] == 1:
                        l_shift_count += 1
                    if r[r_row][m_col] == 1 and m[m_row][r_col] == 1:
                        r_shift_count += 1
            return max(l_shift_count, r_shift_count)
        
        max_ones = 0
        for yshift in range(n):
            for xshift in range(n):
                max_ones = max(max_ones, shift_count(xshift, yshift, img1, img2))
                max_ones = max(max_ones, shift_count(xshift, yshift, img2, img1))
        return max_ones

#using linear transformation, O(n**4) worst, considering only ones
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a, b = [], []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    a.append((i, j))
                if img2[i][j] == 1:
                    b.append((i, j))
        ans = 0
        d = defaultdict(int)
        for t1 in a:
            for t2 in b:
                v = (t2[0]-t1[0], t2[1]-t1[1])
                d[v] += 1
                ans = max(ans, d[v])
        return ans

