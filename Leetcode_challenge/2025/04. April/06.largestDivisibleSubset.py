'''
368. Largest Divisible Subset
Solved
Medium
Topics
Companies
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
        n = len(nums)
        dp = [(1, -1)]*n
        max_len, max_index = 1, 0
        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and dp[j][0]+1 > dp[i][0]:
                    dp[i] = (dp[j][0]+1, j)
                    if dp[i][0] > max_len:
                        max_len, max_index = dp[i][0], i
                        
        sub_set, i = [], max_index
        while i != -1:
            sub_set.append(nums[i])
            i = dp[i][1]

        return sub_set
