'''
Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
 
Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
   Hide Hint #1  
Say f[i] is the final cost to climb to the top from step i. Then f[i] = cost[i] + min(f[i+1], f[i+2]).
'''

# class Solution:
#     def minCostClimbingStairs(self, cost: [int]) -> int:
#         dp = [None for _ in range(len(cost))]
#         dp[0], dp[1] = cost[0], cost[1]
#         for i in range(2, len(cost)):
#             dp[i] = cost[i] + min(dp[i-1], dp[i-2])
#         return min(dp[-1], dp[-2])

# from fastest
class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)

cost = [10,15,20]
# Output: 15
cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6

s = Solution()
print(s.minCostClimbingStairs(cost))
