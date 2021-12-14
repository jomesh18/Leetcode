'''
416. Partition Equal Subset Sum
Medium

6243

101

Add to List

Share
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
Accepted
370,280
Submissions
805,945
'''
#brute force, O(2**n)
# class Solution:
#     def canPartition(self, nums: [int]) -> bool:
#         def helper(i, sum1, sum2):
#             # print(sum1, sum2)
#             if i >= len(nums): return sum1 == sum2
#             return helper(i+1, sum1+nums[i], sum2) or helper(i+1, sum1, sum2+nums[i])
#         return helper(0, sum1=0, sum2=0)

#optimized brute force (return if sum in odd)
# class Solution:
#     def canPartition(self, nums: [int]) -> bool:
#         def subsetSum(i, s):
#             if s == 0: return True
#             if i >= len(nums) or s<0: return False
#             return subsetSum(i+1, s-nums[i]) or subsetSum(i+1, s)
#         total_sum = sum(nums)
#         return total_sum & 1 == 0 and subsetSum(0, total_sum//2)

# class Solution:
#     def canPartition(self, nums: [int]) -> bool:
#         dp = {}
#         def subsetSum(i, s):
#             if s == 0: return True
#             if i >= len(nums) or s<0: return False
#             if (i, s) in dp: return dp[(i, s)]
#             ans = subsetSum(i+1, s-nums[i]) or subsetSum(i+1, s)
#             dp[(i, s)] = ans
#             return ans
#         total_sum = sum(nums)
#         return total_sum & 1 == 0 or subsetSum(total_sum//2)


#tabulation 2d approach
class Solution:
    def canPartition(self, nums: [int]) -> bool:
        s = sum(nums)
        if s & 1 == 1: return False
        s >>= 1
        dp = [[False for _ in range(s+1)] for _ in range(len(nums)+1)]
        dp[0][0] = True
        # for i in range(s+1):
        #     dp[0][i] = False
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, s+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] |= dp[i-1][j-nums[i-1]]
        return dp[len(nums)][s]

#tabulation 1d approach
class Solution:
    def canPartition(self, nums: [int]) -> bool:
        s = sum(nums)
        if s & 1: return False
        s >>= 1
        dp = [True] + [False for _ in range(s)]

        for num in nums:
            for j in range(s+1):
                dp[j] |= dp[j-num]
        return dp[s]


nums = [1,5,11,5]
# Output: true

# nums = [1,2,3,5]
# Output: false

nums = [i for i in range(1, 201)]


sol = Solution()
print(sol.canPartition(nums))
