'''
39. Combination Sum
Medium

9751

214

Add to List

Share
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
Accepted
1,000,107
Submissions
1,548,079
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dp = [1] + [0] * (target+1)
        # for c in candidates:
        #     for i in range(c, target+1):
        #         dp[i] += dp[i-c]
        # return dp[target]
        
        self.ans = []
        def dfs(s, arr, i):
            if s > target: return
            if s == target:
                self.ans.append(arr)
                return
            for k in range(i, len(candidates)):
                dfs(s+candidates[k], arr+[candidates[k]], k)
        dfs(0, [], 0)
        return self.ans