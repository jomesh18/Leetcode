'''
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                max_profit = max(prices[i]-lowest, max_profit)
        return max_profit