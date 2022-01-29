'''
84. Largest Rectangle in Histogram
Hard

8772

131

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
Accepted
462,567
Submissions
1,153,939
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        less_from_left = [0] * l
        less_from_right = [0] * l
        
        less_from_left[0] = -1
        less_from_right[-1] = l
        
        for i in range(1, l):
            p = i-1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_from_left[p]
            less_from_left[i] = p
        
        for i in range(l-2, -1, -1):
            p = i+1
            while p < l and heights[p] >= heights[i]:
                p = less_from_right[p]
            less_from_right[i] = p
        
        ans = 0
        for i in range(l):
            ans = max(ans, heights[i]*(less_from_right[i] - less_from_left[i] - 1))
        return ans
            