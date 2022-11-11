'''
Maximum Product Subarray

Solution
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix = nums[0], nums[-1]
        ans = max(prefix, suffix)
        for i in range(1, len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[-i-1] * (suffix or 1)
            ans = max(ans, prefix, suffix)
        return ans


#memo, recursive
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs_max(i, must_pick):
            if i == n:
                return 1 if must_pick else float('-inf')
            if (i, must_pick) in memo: return memo[(i, must_pick)]
            if must_pick:
                memo[(i, must_pick)] = max(1, nums[i]*(dfs_max(i+1, True) if nums[i] >= 0 else dfs_min(i+1)))
            else:
                memo[(i, must_pick)] = max(dfs_max(i+1, False), nums[i]*(dfs_max(i+1, True) if nums[i] >= 0 else dfs_min(i+1)))
            return memo[(i, must_pick)]
        def dfs_min(i):
            if i == n:
                return 1
            return nums[i]*(dfs_min(i+1) if nums[i] >= 0 else dfs_max(i+1, True))
        return dfs_max(0, False)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, dpmax, dpmin = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            tmax, tmin = dpmax, dpmin
            dpmax = max(nums[i], nums[i]*(tmax if nums[i] >= 0 else tmin))
            dpmin = min(nums[i], nums[i]*(tmin if nums[i] >= 0 else tmax))
            ans = max(ans, dpmax)
        return ans