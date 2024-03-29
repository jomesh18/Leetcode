'''
629. K Inverse Pairs Array
Hard

1809

209

Add to List

Share
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

Constraints:

1 <= n <= 1000
0 <= k <= 1000
Accepted
55,580
Submissions
128,744
'''
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9+7
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    val = (dp[i-1][j] - (dp[i-1][j-i] if j-i >= 0 else 0) + mod) % mod
                    dp[i][j] = (val + dp[i][j-1]) % mod
        return (dp[n][k] - (0 if k <= 0 else dp[n][k-1]) + mod) % mod