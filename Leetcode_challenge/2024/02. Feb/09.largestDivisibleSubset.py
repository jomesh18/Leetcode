'''
368. Largest Divisible Subset
Medium

5328

224

Add to List

Share
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = [nums[0]]
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if not (nums[i] % nums[j]) and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j]+[nums[i]]
                    if len(dp[i]) > len(ans):
                        ans = dp[i]
        return ans
        