'''
3578. Count Partitions With Max-Min Difference at Most K
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]
Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
 

Constraints:

2 <= nums.length <= 5 * 104
1 <= nums[i] <= 109
0 <= k <= 109
'''
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        dp = [0]*(n+1)
        prefix = [0]*(n+1)
        dp[0] = 1
        prefix[0] = 1
        cnt = SortedList()
        j = 0
        for i in range(n):
            cnt.add(nums[i])
            while j<= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j += 1
            dp[i+1] = (prefix[i] - (prefix[j-1] if j > 0 else 0)) % MOD
            prefix[i+1] = (prefix[i] + dp[i+1]) % MOD
        return dp[n]
