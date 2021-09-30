'''
Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

 

Constraints:

    1 <= k <= nums.length <= 16
    1 <= nums[i] <= 104
    The frequency of each element is in the range [1, 4].

   Hide Hint #1  
We can figure out what target each subset must sum to. Then, let's recursively search, where at each call to our function, we choose which of k subsets the next value will join.
'''
class Solution:
    def canPartitionKSubsets(self, nums: [int], k: int) -> bool:
        sums = [0]*k
        subsum = sum(nums) / k
        nums.sort(reverse=True)
        l = len(nums)
        
        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False        
        
        return walk(0)

nums = [4,3,2,3,5,2,1]
k = 4
# Output: true

nums = [1,2,3,4]
k = 3
# # Output: false

sol = Solution()
print(sol.canPartitionKSubsets(nums, k))
