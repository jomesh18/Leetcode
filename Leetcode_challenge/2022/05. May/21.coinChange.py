'''
322. Coin Change
Medium

11914

275

Add to List

Share
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
Accepted
1,025,495
Submissions
2,523,947
'''
#bfs
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        q = [amount]
        level = 0
        visited = {amount}
        while q:
            # print(q)
            next_q = []
            for amount in q:
                for coin in coins:
                    curr_amount = amount-coin
                    if curr_amount == 0: return level + 1
                    if curr_amount < 0: continue
                    if curr_amount not in visited:
                        visited.add(curr_amount)
                        next_q.append(curr_amount)
            q = next_q
            level += 1

        return -1


#dp solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[float("inf")]*amount
        
        for i in range(1, amount+1):
            dp[i] = min(dp[i-c] if i-c>=0 else float("inf") for c in coins) + 1
        
        return dp[amount] if dp[amount] != float('inf') else -1