'''
Burst Balloons

Solution
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
1 <= n <= 300
0 <= nums[i] <= 100
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def helper(start, end, left, right, score):
            if start > end: return 0
            if (start, end, score) in memo: return memo[(start, end, score)]
            curr = 0
            for i in range(start, end+1):
                t = (nums[i] * left * right)
                l = helper(start, i-1, left, nums[i], score)
                r = helper(i+1, end, nums[i], right, score)
                curr = max(curr, t + l + r)
            memo[(start, end, score)] = curr+score
            return curr + score
        return helper(0, n-1, 1, 1, 0)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] +  nums + [1]
        n = len(nums)
    
        dp = [[0]*n for _ in range(n)]
        
        for k in range(2, n):
            for left in range(n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], nums[i]*nums[left]*nums[right]+dp[left][i]+dp[i][right])
        return dp[0][n-1]
    