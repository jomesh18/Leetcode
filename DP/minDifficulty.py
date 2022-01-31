'''

'''

class Solution:
    def minDifficulty(self, jobDifficulty: [int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        def helper(curr_difficulty, i, days_left):
            if days_left == 0:
                return curr_difficulty

            diff = float("inf")
            for k in range(i+1, len(jobDifficulty)-days_left+2):
                diff = min(diff, helper(curr_difficulty+max(jobDifficulty[i:k]), k, days_left-1))
            return diff
            
        return helper(0, 0, d)

jobDifficulty = [6,5,4,3,2,1]
d = 2
#Output: 7

jobDifficulty = [9,9,9]
d = 4
# Output: -1

jobDifficulty = [1,1,1]
d = 3
# Output: 3

jobDifficulty = [11,111,22,222,33,333,44,444]
d = 6
# Output: 843

sol = Solution()
print(sol.minDifficulty(jobDifficulty, d))
