'''
Coin Change

Solution
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
# tle on coins = [186,419,83,408], amount = 6249
# class Solution:
#     def coinChange(self, coins: [int], amount: int) -> int:
#         coins.sort(reverse=True)
#         self.ans = float("inf")
#         self.found = False
#         def dfs(total, count):
#             print(total, count)
#             if total > amount: return
#             if total == amount:
#                 self.ans = min(count, self.ans)
#                 self.found = True
#                 return
#             for i in coins:
#                 if not self.found:
#                     dfs(total+i, count+1)

#         dfs(0, 0)
#         return self.ans if self.ans != float("inf") else -1
        
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        curr = amount
        count = 1
        i = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0: continue
                else: dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


coins = [1,2,5,7, 9, 11, 13, 17, 19, 23, 29, 31]
amount = 10000
# Output: 324

coins = [186,419,83,408]
amount = 6249
# Output: 20

coins = [1,2,5]
amount = 11
# # Output: 3

coins = [2]
amount = 3
# # Output: -1

coins = [1]
amount = 0
# Output: 0

sol = Solution()
print(sol.coinChange(coins, amount))
