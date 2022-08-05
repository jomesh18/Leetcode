'''
377. Combination Sum IV
Medium

4143

453

Add to List

Share
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}
        def backtrack(curr):
            if curr in memo: return memo[curr]
            if curr < 0: return 0
            if curr == 0:
                return 1
            ans = 0
            for k in range(len(nums)):
                ans += backtrack(curr-nums[k])
            memo[curr] = ans
            return ans
        return backtrack(target)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(target + 1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i - j]
        return dp[-1]