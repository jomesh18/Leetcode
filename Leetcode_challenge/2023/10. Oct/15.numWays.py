'''
1269. Number of Ways to Stay in the Same Place After Some Steps
Hard

1456

62

Add to List

Share
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8
 

Constraints:

1 <= steps <= 500
1 <= arrLen <= 106
'''
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(steps, arrLen)
        dp = [[0]*arrLen for _ in range(steps+1)]
        dp[0][0] = 1
        mod = 10**9+7
        for s in range(1, steps+1):
            for i in range(arrLen):
                dp[s][i] = dp[s-1][i]
                if i+1 < arrLen:
                    dp[s][i] = (dp[s][i] + dp[s-1][i+1])% mod
                if i != 0:
                    dp[s][i] = (dp[s][i] + dp[s-1][i-1])% mod
        
        return dp[steps][0]