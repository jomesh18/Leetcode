'''
152. Maximum Product Subarray
Medium

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

 

Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''
# O(n), O(1)
class Solution:
    def maxProduct(self, nums: [int]) -> int:
        ans = nums[0]
        min_ = nums[0]
        max_ = nums[0]
        for i in range(1, len(nums)):
        	min_, max_ = min(nums[i], min_*nums[i], max_*nums[i]), max(nums[i], min_*nums[i], max_*nums[i])
        	ans = max(ans, max_)
        	# print(min_, max_, ans)
        return ans

'''
Calculate prefix product in A.
Calculate suffix product in A.
Return the max.
'''

class Solution:
    def maxProduct(self, nums: [int]) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


nums = [2,3,-2,4]
# Output: 6

nums = [-2,0,-1]
# # # Output: 0

nums = [-2,3,-4]
# # # Output: 24

nums = [0, -2, 3, -4, 0]
# # # Output: 24

nums = [2,-5,-2,-4,3]
# Output: 24

sol = Solution()
print(sol.maxProduct(nums))
