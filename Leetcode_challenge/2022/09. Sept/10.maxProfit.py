'''
188. Best Time to Buy and Sell Stock IV
Hard

5604

188

Add to List

Share
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
Accepted
317,827
Submissions
848,742
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # memo = {}
        # def helper(i, last_price, rem):
        #     if i == len(prices) or rem == 0: return 0
        #     if (i, last_price, rem) in memo: return memo[(i, last_price, rem)]
        #     if last_price == -1:
        #         ans = max(helper(i+1, i, rem), helper(i+1, -1, rem))
        #     else:
        #         ans = 0
        #         for p in range(i, len(prices)):
        #             if prices[p] > prices[last_price]:
        #                 ans = max(ans, prices[p] - prices[last_price] + helper(p+1, -1, rem-1))
        #     memo[(i, last_price, rem)] = ans
        #     return ans
        # return helper(0, -1, k)
        
#         l = len(prices)
#         dp = [[0]*l for _ in range(k+1)]
        
#         for i in range(1, k+1):
#             for j in range(1, l):
#                 dp[i][j] = dp[i][j-1]
#                 for k in range(j):
#                     dp[i][j] = max(dp[i][j], prices[j]-prices[k] + dp[i-1][k])
#         # print(dp)
#         return dp[-1][-1]

        l = len(prices)
        dp = [[0]*l for _ in range(k+1)]
        
        for i in range(1, k+1):
            maxdiff = -prices[0]
            for j in range(1, l):
                dp[i][j] = max(dp[i][j-1], prices[j] + maxdiff)
                maxdiff = max(maxdiff, dp[i-1][j]-prices[j])
        # print(dp)
        return dp[-1][-1]