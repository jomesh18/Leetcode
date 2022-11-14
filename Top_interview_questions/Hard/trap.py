'''
Trapping Rain Water

Solution
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
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = [height[0]]+[0]*(n-1)
        for i in range(1, n):
            ans[i] = max(ans[i-1], height[i])
        right = [0]*(n-1)+[height[n-1]]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        # print(ans)
        # print(right)
        res = 0
        for i in range(n):
            res += min(ans[i], right[i])-height[i]
        return res

# monotonic decreasing stack
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                k = stack.pop()
                ans += 0 if not stack else (min(height[i], height[stack[-1]])-height[k])*(i-1-stack[-1])
                # print(i, ans)
            stack.append(i)
        return ans

# using two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, left_max, right_max, ans = 0, len(height)-1, 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max-height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max-height[right])
                right -= 1
        return ans