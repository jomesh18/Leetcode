'''
416. Partition Equal Subset Sum
Solved
Medium
Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # s = sum(nums)
        # if s & 1: return False
        # s //= 2
        # memo = {}
        # def can(i, s):
        #     if s == 0: return True
        #     if i == len(nums) or s < 0:
        #         return False
        #     if (i, s) in memo: return memo[(i, s)]
        #     taking = can(i+1, s-nums[i])
        #     not_taking = can(i+1, s)
        #     memo[(i, s)] = taking or not_taking
        #     return memo[(i, s)]
        
        # return can(0, s)

        all_s = sum(nums)
        if all_s & 1: return False
        s = all_s // 2
        n = len(nums)
        dp = [[False]*(s+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        for i in range(n-1, -1, -1):
            for su in range(1, s+1):
                if ((i + 1) < n) and (su >= nums[i]):
                    dp[i][su] = dp[i+1][su-nums[i]]
                if (i+1) < n:
                    dp[i][su] |= dp[i+1][su]
        return dp[0][s]
