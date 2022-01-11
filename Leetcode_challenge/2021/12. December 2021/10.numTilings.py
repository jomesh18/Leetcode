'''
790. Domino and Tromino Tiling
Medium

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:

Input: n = 3
Output: 5
Explanation: The five different ways are show above.

Example 2:

Input: n = 1
Output: 1

 

Constraints:

    1 <= n <= 1000

Accepted
29,771
Submissions
67,639
'''
# by archit91
# https://leetcode.com/problems/domino-and-tromino-tiling/discuss/1620975/C%2B%2BPython-Simple-Solution-w-Images-and-Explanation-or-Optimization-from-Brute-Force-to-DP
# https://leetcode.com/problems/domino-and-tromino-tiling/discuss/1620809/PythonJAVACC%2B%2B-DP-oror-Visualized-Explanation-oror-100-Faster-oror-O(N)

#recursive
# from start to end
# class Solution:
#     def numTilings(self, n: int) -> int:
#         mod = 1e9+7
#         def solve(i, previous_gap):
#             if i > n: return 0
#             if i == n: return not previous_gap
#             if previous_gap:
#                 return solve(i+1, False) + solve(i+1, True)
#             return solve(i+1, False) + solve(i+2, False) + 2*solve(i+2, True)
#         return solve(0, False)%mod

# # from end to start
# class Solution:
#     def numTilings(self, n: int) -> int:
#         mod = 1e9+7
#         def solve(i, previous_gap):
#             if i < 0: return 0
#             if i == 0: return not previous_gap
#             if previous_gap:
#                 return solve(i-1, False) + solve(i-2, True)
#             return solve(i-1, False) + solve(i-2, False) + 2*solve(i-2, True)
#         return solve(n, False)%mod


#recursive with memoization
# from start to end
# import sys
# sys.setrecursionlimit(2100)
# class Solution:
#     def numTilings(self, n: int) -> int:
#         mod = 1e9+7
#         dp = {}
#         def solve(i, previous_gap):
#             if i > n: return 0
#             if i == n: return not previous_gap
#             if (i, previous_gap) in dp: return dp[(i, previous_gap)]
#             if previous_gap:
#                 ans = solve(i+1, False) + solve(i+1, True)
#                 dp[(i, previous_gap)] = ans%mod
#                 return ans%mod
#             ans = solve(i+1, False) + solve(i+2, False) + 2*solve(i+2, True)
#             dp[(i, previous_gap)] = ans%mod
#             return ans%mod
#         return int(solve(0, False))

# (Dynamic Programming - Tabulation)
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1e9+7
        dp = [[0, 0] for _ in range(n+2)]
        dp[1] = [1, 1]
        dp[2] = [2, 2]
        for i in range(3, n+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + 2*dp[i-2][1])%mod
            dp[i][1] = (dp[i-1][1] + dp[i-1][0])%mod
        return int(dp[n][0])

#space optimized dp using arr
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1e9+7
        dp = [[0, 0] for _ in range(3)]
        dp[1], dp[2] = [1, 1], [2, 2]
        for i in range(3, n+1):
            dp[i%3][0] = (dp[(i-1)%3][0]+ dp[(i-2)%3][0] + 2*dp[(i-2)%3][1])%mod
            dp[i%3][1] = (dp[(i-1)%3][0] + dp[(i-1)%3][1])%mod
        return int(dp[n%3][0])

#space optimized dp using separate variables
class Solution:
    def numTilings(self, n: int) -> int:
        if n <=2: return n
        mod = 1e9+7
        filled_prev, gap_prev, filled_prev2, gap_prev2 = 2, 2, 1, 1
        for i in range(3, n+1):
            filled = (filled_prev + filled_prev2 + 2*gap_prev2)%mod
            gap = (filled_prev + gap_prev)%mod
            filled_prev, gap_prev, filled_prev2, gap_prev2 = filled, gap, filled_prev, gap_prev

        return int(filled_prev)

n = 3
# Output: 5

n = 1
# Output: 1

n = 50
#Output: 451995196

n = 1000
#Output: 979232805

sol = Solution()
print(sol.numTilings(n))
