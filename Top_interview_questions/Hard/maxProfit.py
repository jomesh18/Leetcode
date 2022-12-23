class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, memo = len(prices), {}
        def helper(i, bought):
            if (i, bought) not in memo:
                if i >= n:
                    return 0
                if bought:
                    ans = prices[i] + helper(i+2, False)
                else:
                    ans = -prices[i] + helper(i+1, True)
                memo[(i, bought)] = max(ans, helper(i+1, bought))
            return memo[(i, bought)]
        return helper(0, False)