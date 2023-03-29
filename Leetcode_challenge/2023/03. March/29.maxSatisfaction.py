'''
1402. Reducing Dishes
Hard

2181

229

Add to List

Share
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

 

Example 1:

Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.
Example 2:

Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
Example 3:

Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People do not like the dishes. No dish is prepared.
 

Constraints:

n == satisfaction.length
1 <= n <= 500
-1000 <= satisfaction[i] <= 1000
'''
# O(n*n)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        ans = 0
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += (j-i+1)*satisfaction[j]
            ans = max(ans, curr)
        return ans

# memo O(n*n)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        ans = 0
        memo = {}
        def helper(i, t):
            if i == n:
                return 0
            if (i, t) in memo: return memo[(i, t)]
            cook = satisfaction[i]*t + helper(i+1, t+1)
            skip = helper(i+1, t)
            memo[(i, t)] = max(cook, skip)
            return memo[(i, t)]
        
        return max(ans, helper(0, 1))


# O(n*n)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        ans = 0
        dp = [[0]*(n+2) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for t in range(1, n+1):
                dp[i][t] = max(satisfaction[i]*t+dp[i+1][t+1], dp[i+1][t])
        return dp[0][1]


# O(nlogn)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        max_satisfaction = 0
        suff_sum = 0
        for i in range(n-1, -1, -1):
            suff_sum += satisfaction[i]
            if suff_sum <= 0:
                break
            max_satisfaction += suff_sum
        return max_satisfaction