'''Trapping Rain Water
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
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''

class Solution:
    def trap(self, height: [int]) -> int:
        # n = len(height)
        # if n == 0 or n == 1:
        #     return 0
        # l, r = 0, 1
        # total, temp = 0, 0
        # while l<n:
        #     if r == n:
        #         if l>=(n-2):
        #             break
        #         l += 1
        #         r = l
        #         temp = 0
        #     if height[r] >= height[l]:
        #         total += temp
        #         temp = 0
        #         l = r
        #     else:
        #         temp += (height[l]-height[r])
        #     r += 1
        # return total
        n = len(height)
        l, r = 0, n-1
        ans = 0
        l_max, r_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    ans += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    ans += r_max - height[r]
                r -= 1
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# # Output: 6

height = [4,2,0,3,2,5]
# # Output: 9

height = [4,2,3]
#Output: 1

sol = Solution()
print(sol.trap(height))
