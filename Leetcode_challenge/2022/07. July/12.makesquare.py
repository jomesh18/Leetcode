'''
473. Matchsticks to Square
Medium

2213

166

Add to List

Share
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108
Accepted
92,587
Submissions
231,467
'''
#my backtrack solution, Runtime: 5541 ms, faster than 22.79% of Python3 online submission
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0: return False
        a = s//4
        sides = 0
        n = len(matchsticks)
        @lru_cache(None)
        def backtrack(mask, curr_s):
            if not mask and curr_s == a:
                return True
            if curr_s == a:
                curr_s = 0
            ans = False
            for i in range(n):
                if mask & (1<<i):
                    curr_s += matchsticks[i]
                    if curr_s <= a:
                        ans |= backtrack(mask^(1<<i), curr_s)
                    curr_s -= matchsticks[i]
            return ans
        return backtrack((1<<n)-1, 0)
