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
# class Solution:
#     def largestRectangleArea(self, heights: [int]) -> int:
#         stack, area, max_area = [], 0, 0
#         i = 0
#         while i<len(heights):
#             if not stack or stack[-1] <= heights[i]:
#                 stack.append(i)
#                 i += 1
#             else:
#                 top_of_stack = stack.pop()
#                 ares = heights[top_of_stack] * ((i-stack[-1]-1) if stack else i)
#                 max_area = max(max_area, area)
#         while stack:
#             top_of_stack = stack.pop()
#             ares = heights[top_of_stack] * ((i-stack[-1]-1) if stack else i)
#             max_area = max(max_area, area)

#         return max_area

#from geeksforgeeks
class Solution:
    def largestRectangleArea(self, heights):
         
        # This function calculates maximum
        # rectangular area under given
        # histogram with n bars

        # Create an empty stack. The stack
        # holds indexes of histogram[] list.
        # The bars stored in the stack are
        # always in increasing order of
        # their heights.
        stack = list()

        max_area = 0 # Initialize max area

        # Run through all bars of
        # given histogram
        index = 0
        while index < len(heights):
  
            # If this bar is higher
            # than the bar on top
            # stack, push it to stack

            if (not stack) or (heights[stack[-1]] <= heights[index]):
                stack.append(index)
                index += 1

            # If this bar is lower than top of stack,
            # then calculate area of rectangle with
            # stack top as the smallest (or minimum
            # height) bar.'i' is 'right index' for
            # the top and element before top in stack
            # is 'left index'
            else:
                # pop the top
                top_of_stack = stack.pop()
     
                # Calculate the area with
                # histogram[top_of_stack] stack
                # as smallest bar
                area = (heights[top_of_stack] *((index - stack[-1] - 1) if stack else index))
     
                # update max area, if needed
                max_area = max(max_area, area)
     
        # Now pop the remaining bars from
        # stack and calculate area with
        # every popped bar as the smallest bar
        while stack:
             
            # pop the top
            top_of_stack = stack.pop()
     
            # Calculate the area with
            # histogram[top_of_stack]
            # stack as smallest bar
            area = (heights[top_of_stack] *
                  ((index - stack[-1] - 1)
                    if stack else index))
     
            # update max area, if needed
            max_area = max(max_area, area)
     
        # Return maximum area under
        # the given histogram
        return max_area

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
