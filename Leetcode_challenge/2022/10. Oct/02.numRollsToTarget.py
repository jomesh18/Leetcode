'''
1155. Number of Dice Rolls With Target Sum
Medium

3434

111

Add to List

Share
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.
 

Constraints:

1 <= n, k <= 30
1 <= target <= 1000
Accepted
161,034
Submissions
302,323
'''
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        memo = {}
        def dfs(rem, curr_sum):
            if rem*k + curr_sum < target: return 0
            if (rem, curr_sum) in memo: return memo[(rem, curr_sum)]
            if curr_sum > target: return 0
            if rem == 0 and curr_sum == target: return 1
            ans = 0
            for val in range(k, 0, -1):
                ans += dfs(rem-1, curr_sum+val)
            memo[(rem, curr_sum)] = ans
            return ans%MOD
        return dfs(n, 0)
