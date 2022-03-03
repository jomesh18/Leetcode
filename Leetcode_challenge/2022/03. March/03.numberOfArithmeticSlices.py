'''
413. Arithmetic Slices
Medium

3157

235

Add to List

Share
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
Accepted
191,730
Submissions
302,858
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: [int]) -> int:
        diff = [None]*(len(nums)-1)
        for i in range(len(nums)-1):
            diff[i] = nums[i+1] - nums[i]
        i = 0
        prev = 0
        ans = 0
        while i < len(diff):
            if diff[i] != diff[prev]:
                c = i - prev
                if c >= 2:
                    c-= 1
                    c = c*(c+1)//2
                    ans += c
                prev = i
            i += 1
        if i != prev:
            c = i - prev
            if c >= 2:
                c-= 1
                c = c*(c+1)//2
                ans += c
        return ans

#without diff array
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        i, j = 2, 1
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] != nums[j]-nums[j-1]:
                j = i
            res += (i-j)
        return res

#using dp
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0] * l
        ans = 0
        for i in range(2, l):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans