'''
312. Burst Balloons
Hard

4872

141

Add to List

Share
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100
Accepted
159,587
Submissions
288,586
'''
#naive, backtracking
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         self.score = 0
#         def dfs(balloons, curr_score):
#             if len(balloons) == 2:
#                 self.score = max(self.score, curr_score)
#             for i in range(1, len(balloons)-1):
#                 temp = balloons[i]*balloons[i-1]*balloons[i+1]
#                 curr_score += temp
#                 dfs(balloons[:i]+balloons[i+1:], curr_score)
#                 curr_score -= temp
#         dfs([1]+nums+[1], 0)
#         return self.score

#divide and conquer with memoization
class Solution:
    def maxCoins(self, nums: [int]) -> int:
        new_nums = [0]*(len(nums)+2)
        n = 1
        for x in nums:
            if x > 0:
                new_nums[n] = x
                n += 1
        new_nums[0] = 1
        new_nums[n] = 1
        n += 1
        memo = [[0]*n for _ in range(n)]

        def burst(left, right):
            if left + 1 == right: return 0
            if memo[left][right] > 0 : return memo[left][right]
            ans = 0
            for i in range(left+1, right):
                ans = max(ans, new_nums[left]*new_nums[i]*new_nums[right] + burst(left, i) + burst(i, right))
            memo[left][right] = ans
            return ans
        return burst(0, n-1)    


# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums, n = [1] + nums + [1], len(nums) + 2
#         dp = [[0] * n for _ in range(n)]
        
#         for i in range(n - 2, -1, -1):
#             for j in range(i + 2, n):
#                 dp[i][j] = max(nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
        
#         return dp[0][n-1]

nums = [3,1,5,8]
# Output: 167

nums = [1,5]
# Output: 10

sol = Solution()
print(sol.maxCoins(nums))
