'''
Coin Change 2

Solution
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
'''
#top down memo
class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        def helper(i, amount):
            # print(i, amount)
            if amount < 0: return 0
            if i < 0 : return 0
            if amount == 0: return 1
            if dp[i][amount] != -1: return dp[i][amount]
            if amount-coins[i] >= 0:
                dp[i][amount] = helper(i, amount-coins[i])+helper(i-1, amount)
            else:
                dp[i][amount] = helper(i-1, amount)
            return dp[i][amount]

        ans = helper(len(coins)-1, amount)
        # print(dp)
        return ans

#bottom up dp
# class Solution:
#     def change(self, amount: int, coins: [int]) -> int:
#         dp = [1]+[0]*(amount)
#         for c in coins:
#             for i in range(amount+1):
#                 if i-c >= 0:
#                     dp[i] += dp[i-c]
#         print(dp)
#         return dp[amount]


amount = 5
coins = [1,2,5]
# Output: 4

# amount = 3
# coins = [2]
# # # # Output: 0

# amount = 10
# coins = [10]
# # # Output: 1

sol = Solution()
print(sol.change(amount, coins))
