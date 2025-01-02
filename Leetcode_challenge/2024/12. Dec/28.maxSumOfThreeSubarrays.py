'''
689. Maximum Sum of 3 Non-Overlapping Subarrays
Solved
Hard
Topics
Companies
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically smaller.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)
'''
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = [0]*(len(nums)-k+1)
        sums[0] = sum(nums[:k])
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] + nums[i+k-1] - nums[i-1]

        memo = {}
        def helper(i, rem):
            if rem == 0:
                return 0
            if i+rem*k > len(nums):
                return float('-inf')
            if (i, rem) in memo: return memo[(i, rem)]
            taking = sums[i] + helper(i+k, rem-1)
            not_taking = helper(i+1, rem)
            memo[(i, rem)] = max(taking, not_taking)
            return memo[(i, rem)]

        helper(0, 3)
        
        indices = []
        def dfs(i, rem, memo, indices):
            if rem == 0 or i >= len(nums):
                return 
            taking = sums[i] + helper(i+k, rem-1)
            not_taking = helper(i+1, rem)
            if taking >= not_taking:
                indices.append(i)
                dfs(i+k, rem-1, memo, indices)
            else:
                dfs(i+1, rem, memo, indices)

        dfs(0, 3, memo, indices)
        return indices
