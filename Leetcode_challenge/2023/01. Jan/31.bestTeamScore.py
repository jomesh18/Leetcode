'''
1626. Best Team With No Conflicts
Medium

1833

54

Add to List

Share
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

Example 1:

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.
Example 2:

Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
Example 3:

Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 
 

Constraints:

1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 106
1 <= ages[i] <= 1000
'''
# O(n*n) rejected, memo is dict
# top-down memo
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        new = [(u, v) for u, v in zip(ages, scores)]
        new.sort()
        memo = {}
        def helper(i, prev):
            if i >= len(new):
                return 0
            if (i, prev) in memo: return memo[(i, prev)]
            ans = 0
            if prev is None or new[i][1] >= new[prev][1]:
                ans = new[i][1] + helper(i+1, i)
            ans = max(ans, helper(i+1, prev))
            memo[(i, prev)] = ans
            return ans
        return helper(0, None)

# O(n*n), accepted, memo is list 7.8k ms
# top-down memo
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        new = [(u, v) for u, v in zip(ages, scores)]
        new.sort()
        dp = [[-1]*(len(new)+1) for _ in range(len(new)+1)]
        def helper(i, prev):
            if i >= len(new):
                return 0
            if dp[i][prev] != -1: return dp[i][prev]
            if prev == -1 or new[i][1] >= new[prev][1]:
                dp[i][prev] = new[i][1] + helper(i+1, i)
            dp[i][prev] = max(dp[i][prev], helper(i+1, prev))
            return dp[i][prev]
        return helper(0, -1)

# O(n*n), accepted, fast, 1.7k ms
# bottom up dp
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores = [x for _,x in sorted(zip(ages, scores))]
        dp = scores.copy()
        ans = scores[0]
        for i in range(1, len(scores)):
            for j in range(i):
                if scores[j] <= scores[i]:
                    dp[i] = max(dp[i], scores[i] + dp[j])
            ans = max(dp[i], ans)
        return ans

# O(n*n)
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
                                                #   Example: scores = [4,4,6,5]
                                                #              ages = [2,1,5,1]

        dp = [0]*(1+max(ages))                  #         dp = [0, 0, 0, 0, 0]       
                                                #  score_age = [(4,1), (4,2), (5,1), (6,5)]
        score_age = sorted(zip(scores, ages))
                                                #   score   age     dp
        for score, age in score_age:            #   –––––  –––––    ––––––––––––––––––
                                                #     4      1      [0, 4, 0, 0, 0, 0]
            dp[age] = score + max(dp[:age+1])   #     4      2      [0, 4, 8, 0, 0, 0]
                                                #     5      1      [0, 9, 8, 0, 0, 0]
        return max(dp)                          #     6      5      [0, 9, 8, 0, 0,15] 
                                                #                                   |
                                                #                                 return 

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        max_scores=[0]*(max(ages)+1)
        
        for score, age in sorted(zip(scores, ages)): max_scores[age] = score + max(max_scores[:age + 1])

        return max(max_scores)


# using bit, nlogn + nlogk, where k is the max age, n is the number of players
class BIT:
    def __init__(self, n):
        self.bit = [0]*(n+1)
        
    def update(self, pos, new):
        pos += 1
        while pos < len(self.bit):
            self.bit[pos] = max(self.bit[pos], new)
            pos += (pos & -pos)
    
    def max_(self, pos):
        m = float('-inf')
        pos += 1
        while pos > 0:
            m = max(m, self.bit[pos])
            pos -= (pos & -pos)
        return m
            
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        bit = BIT(max(ages)+1)
        ans = float('-inf')
        for score, age in sorted(zip(scores, ages)):
            curr = bit.max_(age) + score
            bit.update(age, curr)
            ans = max(ans, curr)
        return ans