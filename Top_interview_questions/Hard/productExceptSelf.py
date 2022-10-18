'''
Product of Array Except Self

Solution
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
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suff = [1]*(n+1), [1]*(n+1)
        for i in range(1, n):
            pref[i] = pref[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1]*nums[i+1]
        res = [1]*(n)
        for i in range(n):
            res[i] = pref[i]*suff[i]
        return res

#O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]*n
        for i in range(1, n):
            pref[i] = pref[i-1]*nums[i-1]
        cumu = 1
        for i in range(n-2, -1, -1):
            cumu *= nums[i+1]
            pref[i] *= cumu
        return pref