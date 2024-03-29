'''
879. Profitable Schemes
Hard

975

85

Add to List

Share
There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
 

Constraints:

1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
'''
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        m = len(group)
        memo = {}
        def helper(i, curr_profit, curr_people):
            if i == m:
                return 1 if curr_profit >= minProfit else 0
            if (i, curr_profit, curr_people) in memo: return memo[(i, curr_profit, curr_people)]
            ways = helper(i+1, curr_profit, curr_people)%MOD
            if curr_people + group[i] <= n:
                ways = (ways + helper(i+1, min(minProfit, curr_profit+profit[i]), curr_people+group[i])) % MOD
            memo[(i, curr_profit, curr_people)] = ways
            return ways
        return helper(0, 0, 0)


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        m = len(group)  
        dp = [[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(m+1)]
        
        for people in range(n+1):
            dp[m][people][minProfit] = 1
        
        for i in range(m-1, -1, -1):
            for curr_people in range(n+1):
                for curr_profit in range(minProfit+1):
                    take = (dp[i+1][curr_people+group[i]][min(minProfit, curr_profit+profit[i])] if (curr_people + group[i] <= n) else 0)%MOD
                    dp[i][curr_people][curr_profit] = (dp[i+1][curr_people][curr_profit] + take)%MOD
        
        return dp[0][0][0]