'''
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

#O(n) time, O(1) space, but uses divison operation
# class Solution:
#     def productExceptSelf(self, nums: [int]) -> [int]:
#         total_product = 1
#         zero_pos = -1
#         zero_count = 0
#         for i, num in enumerate(nums):
#             if num:
#                 total_product *= num
#             else:
#                 zero_pos = i
#                 zero_count += 1
#         ans = [0] * len(nums)
#         if zero_count == 1:
#             ans[zero_pos] = total_product
#         elif not zero_count:
#             for i in range(len(nums)):
#                 ans[i] = int(total_product/nums[i])
#         return ans


#O(n) time, O(n) space, using pref, suff
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        pref, suff = [1]*len(nums), [1]*len(nums)
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            pref[i] = product
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            suff[i] = product
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = pref[i] * suff[i]
        return ans

##O(n) time, O(1) space, using pref, suff, two pass
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        ans = [1]*len(nums)
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            ans[i] = product
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            ans[i] *= product
        return ans

##O(n) time, O(1) space, using pref, suff, one pass
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        ans = [1] * len(nums)
        pref_product = 1
        suff_product = 1
        for i in range(len(nums)):
            ans[i] *= pref_product
            pref_product *= nums[i]
            ans[-1-i] *= suff_product
            suff_product *= nums[-1-i]
        return ans

nums = [1,2,3,4]
# Output: [24,12,8,6]

# nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

sol = Solution()
print(sol.productExceptSelf(nums))
