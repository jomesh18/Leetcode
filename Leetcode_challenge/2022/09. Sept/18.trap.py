'''
42. Trapping Rain Water
Hard

22813

307

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
Accepted
1,330,190
Submissions
2,272,703
'''
#two iteration(find left_max, right_max, min, diff)
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]]
        for i in range(1, len(height)):
            left.append(max(height[i], left[-1]))
        r = height[-1]
        s = 0
        for i in range(len(height)-2, -1, -1):
            r = max(height[i], r)
            left[i] = min(r, left[i])
            s += (left[i]-height[i])
        return s

#stack, one iteration
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top = stack.pop()
                if stack:
                    bounded_h = min(height[stack[-1]], h)-height[top]
                    bounded_d = i-stack[-1]-1
                    ans += bounded_h*bounded_d
            stack.append(i)
        return ans

#two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, left_max, right_max, s = 0, len(height)-1, 0, 0, 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    s += left_max-height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    s += right_max-height[right]
                right -= 1
        return s