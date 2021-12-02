'''
 Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

 

Constraints:

    1 <= prices.length <= 3 * 104
    0 <= prices[i] <= 104

'''
#O(n**n) time, space O(n)
# class Solution:
#     def maxProfit(self, prices: [int]) -> int:
#         def calculate(s):
#             if s >= len(prices):
#                 return 0
#             max_ = 0
#             for start in range(s, len(prices)):
#                 max_profit = 0
#                 for i in range(start+1, len(prices)):
#                     if prices[start] < prices[i]:
#                         profit = calculate(i+1) + prices[i] - prices[start]
#                         if profit > max_profit:
#                             max_profit = profit
#                 if max_profit > max_:
#                     max_ = max_profit
#             return max_

#         return calculate(0)


#O(n) time, O(1) space, peak valley approach
# class Solution:
#     def maxProfit(self, prices: [int]) -> int:
#         peak, valley = prices[0], prices[0]
#         max_profit = 0
#         i = 0
#         while i < len(prices) - 1:
#             while i < len(prices)-1 and prices[i] >= prices[i+1]:
#                 i += 1
#             valley = prices[i]
#             while i < len(prices)-1 and prices[i] <= prices[i+1]:
#                 i += 1
#             peak = prices[i]
#             max_profit += peak - valley
#         return max_profit

'''
This solution follows the logic used in Approach 2 itself, but with only a slight variation. 
In this case, instead of looking for every peak following a valley, we can simply go on crawling over 
the slope and keep on adding the profit obtained from every consecutive transaction. 
In the end,we will be using the peaks and valleys effectively, but we need not track the costs 
corresponding to the peaks and valleys along with the maximum profit, but we can directly keep on adding 
the difference between the consecutive numbers of the array if the second number is larger than the first one, 
and at the total sum we obtain will be the maximum profit. This approach will simplify the solution. 
This can be made clearer by taking this example:
'''
# class Solution:
#     def maxProfit(self, prices: [int]) -> int:
#         max_profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 max_profit += prices[i] - prices[i-1]
#         return max_profit


'''
The action we can do on ith day is either buy (if last action is sell), or sell (if last action is buy), or do nothing (not buy, not sell).
'''
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices) == 0: return 0
        lastBuy, lastSold = -prices[0], 0 
        for i in range(1, len(prices)):    
            curBuy = max(lastBuy, lastSold-prices[i])
            curSold = max(lastSold, lastBuy + prices[i])
            lastBuy = curBuy
            lastSold = curSold
        return lastSold


# prices = [7,1,5,3,6,4]
# Output: 7

prices = [1,2,3,4,5]
# Output: 4

# prices = [7,6,4,3,1]
# Output: 0

# prices = [1, 7, 2, 3, 6, 7, 6, 7]
# Output: 12

sol = Solution()
print(sol.maxProfit(prices))
