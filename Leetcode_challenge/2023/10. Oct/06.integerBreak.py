'''
343. Integer Break
Medium

4886

420

Add to List

Share
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        if n % 3 == 0:
            return 3**(n//3)
        if n % 3 == 1:
            return 4*3**(n//3-1)
        if n % 3 == 2:
            return 2*3**(n//3)


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n-1
        memo = {}
        def helper(i):
            if i <= 3: return i
            if i in memo: return memo[i]
            ans = 0
            for j in range(i-1, 1, -1):
                ans = max(ans, j*helper(i-j))
            memo[i] = ans
            return ans
        return helper(n)