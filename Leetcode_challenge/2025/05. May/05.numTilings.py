'''
790. Domino and Tromino Tiling
Solved
Medium
Topics
premium lock icon
Companies
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are shown above.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 1000
'''
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        memo = {}
        def helper(i, is_closed):
            if i == n:
                return 1 if is_closed else 0
            if i > n:
                return 0
            if (i, is_closed) in memo: return memo[(i, is_closed)]

            ans = 0
            if is_closed:
                ans = (ans + helper(i+1, is_closed)) % MOD
                ans = (ans + helper(i+2, is_closed)) % MOD
                ans = (ans + 2*helper(i+1, False)) % MOD
            else:
                ans = (ans + helper(i+1, False)) % MOD
                ans = (ans + helper(i+2, True)) % MOD

            memo[(i, is_closed)] = ans
            return ans

        return helper(0, True)
