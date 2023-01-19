'''
918. Maximum Sum Circular Subarray
Medium

5478

235

Add to List

Share
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0]*n
        suff_sum = nums[-1]
        right_max[-1] = suff_sum
        for i in range(n-2, -1, -1):
            suff_sum += nums[i]
            right_max[i] = max(right_max[i+1], suff_sum)
        
        #kadane's algo to find normal max_sum
        # finding special sum also included
        max_sum = float('-inf')
        curr_sum = float('-inf')
        pre = 0
        sp_sum = nums[0]
        for i, num in enumerate(nums):
            curr_sum = max(num, curr_sum+num)
            max_sum = max(max_sum, curr_sum)
            pre += num
            sp_sum = max(pre+(right_max[i+1] if i+1 < n else 0), sp_sum)
            
        return max(max_sum, sp_sum)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, max_so_far = 0, float('-inf')
        curr_min, min_so_far = 0, float('inf')
        tot_sum = 0
        for num in nums:
            tot_sum += num
            curr_max = max(curr_max+num, num)
            max_so_far = max(max_so_far, curr_max)
            curr_min = min(curr_min+num, num)
            min_so_far = min(min_so_far, curr_min)
        return max_so_far if min_so_far == tot_sum else max(max_so_far, tot_sum - min_so_far)