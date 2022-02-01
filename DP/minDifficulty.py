'''

'''
#my try, top down memoization, accepted Runtime: 6929 ms, faster than 5.01% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
# Memory Usage: 15.1 MB, less than 52.24% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
class Solution:
    def minDifficulty(self, jobDifficulty: [int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        dp = {}
        def helper(i, days_left):
            if (i, days_left) in dp: return dp[(i, days_left)]
            if days_left == 1:
                return max(jobDifficulty[i:])
            diff = float("inf")
            for k in range(i, len(jobDifficulty)-days_left+1):
                diff = min(diff, max(jobDifficulty[i:k+1]) + helper(k+1, days_left-1))
            dp[(i, days_left)] = diff
            return diff
            
        return helper(0, d)


#bottom up dp
class Solution:
    def minDifficulty(self, jobDifficulty: [int], d: int) -> int:
        l = len(jobDifficulty)
        if l < d:
            return -1
        dp = [[0]*(d+1) for _ in range(l+1)]

        for j in range(1, d+1):
            for j in range(l-1, -1, -1):
                dp


jobDifficulty = [6,5,4,3,2,1]
d = 2
#Output: 7

jobDifficulty = [9,9,9]
d = 4
# Output: -1

jobDifficulty = [1,1,1]
d = 3
# Output: 3

# jobDifficulty = [11,111,22,222,33,333,44,444]
# d = 6
# Output: 843

sol = Solution()
print(sol.minDifficulty(jobDifficulty, d))
