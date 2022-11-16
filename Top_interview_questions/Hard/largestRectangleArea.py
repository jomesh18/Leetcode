'''
84. Largest Rectangle in Histogram
Hard

12626

176

Add to List

Share
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
# using lessfromleft and lessfromright, 3 iterations
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lessfromleft = [-1]*n
        for i in range(1, n):
            p = i-1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessfromleft[p]
            lessfromleft[i] = p
        lessfromright = [n]*n
        for i in range(n-2, -1, -1):
            p = i+1
            while p < n and heights[p] >= heights[i]:
                p = lessfromright[p]
            lessfromright[i] = p
        ans = 0
        for i in range(n):
            ans = max((lessfromright[i]-lessfromleft[i]-1)*heights[i], ans)
        return ans

# using stack, one iteration
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        ans = 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i-stack[-1]-1
                ans = max(ans, w*h)
            stack.append(i)
        heights.pop()
        return ans