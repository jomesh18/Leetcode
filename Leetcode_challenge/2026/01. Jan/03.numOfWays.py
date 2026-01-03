'''
1411. Number of Ways to Paint N × 3 Grid
Solved
Hard
Topics
premium lock icon
Companies
Hint
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
Example 2:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
1 <= n <= 5000
'''
class Solution:
    def numOfWays(self, n: int) -> int:
        memo = {}
        MOD = 10 ** 9 + 7
        def helper(i, prev, curr):
            if i == n:
                return 1
            key = (i, prev, curr)
            if key in memo: return memo[key]

            ans = 0
            if len(curr) == 3:
                ans = helper(i+1, curr, '')
            else:
                for j in 'RYG':
                    pos = len(curr)
                    if prev[pos] != j and (not curr or curr[-1] != j):
                        ans = (ans + helper(i, prev, curr+j)) % MOD
            memo[key] = ans
            return ans

        return helper(0, 'aaa', '')
