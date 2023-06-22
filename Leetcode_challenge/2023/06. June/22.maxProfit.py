'''
714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

5694

147

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
'''
# topdown dp, O(n) time, O(n) space
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = [[None]*2 for _ in range(n)]
        def helper(i, bought):
            if i == n and bought:
                return float('-inf')
            if i == n: return 0
            if memo[i][bought]: return memo[i][bought]
            if bought:
                ans = (prices[i]-fee)+helper(i+1, False)
                ans = max(ans, helper(i+1, True))
            else:
                ans = -prices[i] + helper(i+1, True)
                ans = max(ans, helper(i+1, False))
            memo[i][bought] = ans
            return memo[i][bought]
        return max(0, helper(0, False))

# bottom up dp, O(n) time, O(n) space
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)    
        dp = [[0]*2 for _ in range(n+1)]
        dp[n][1] = float('-inf')
        for i in range(n-1, -1, -1):
            dp[i][False] = max(dp[i+1][False], -prices[i]+dp[i+1][True])
            dp[i][True] = max(dp[i+1][True], prices[i]-fee+dp[i+1][False])
        return dp[0][False]

# optimized bottom up dp, O(n) time, O(1) space
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        holding = float('-inf')
        not_holding = 0
        for i in range(n-1, -1, -1):
            new_not_holding = max(not_holding, -prices[i]+holding)
            new_holding = max(holding, prices[i]-fee+not_holding)
            holding, not_holding = new_holding, new_not_holding
        return not_holding