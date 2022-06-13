'''
120. Triangle
Medium

5330

390

Add to List

Share
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
Accepted
439,617
Submissions
851,400
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = triangle[0]
        for row in triangle[1:]:
            t = [0]*len(row)
            for i in range(len(row)):
                t[i] = row[i] + min(ans[i-1] if i>0 else float('inf'), ans[i] if i < len(ans) else float('inf'))
            ans = t[:]
        return min(ans)