'''
 Largest Rectangle in Histogram

Solution
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
class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        stack, area = [], 0
        i = 0
        while i < len(heights):
            while i<len(heights) and (not stack or stack[-1][0] <= heights[i]):
                stack.append((heights[i], i))
                i += 1
                # print(i)
            while stack and i < len(heights) and stack[-1][0] >= heights[i]:
                h, ind = stack.pop()
                area = max(area, h*(i-ind))

        while stack:
            h, ind = stack.pop()
            area = max(area, h*(i-ind))

        return area

heights = [2,1,5,6,2,3]
# Output: 10

heights = [2,4]
Output: 4

# heights = [0,0]
# # Output: 0

heights = [2,1,2]
#Output: 3

sol = Solution()
print(sol.largestRectangleArea(heights))
