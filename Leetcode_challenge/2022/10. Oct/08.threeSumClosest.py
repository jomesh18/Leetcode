'''
16. 3Sum Closest
Medium

7919

440

Add to List

Share
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        if res >= target: return res
        res = sum(nums[-3:])
        if res <= target: return res
        diff = float('inf')
        for i in range(len(nums)-2):
            curr_sum = target-nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                iter_sum = nums[j] + nums[k]
                if iter_sum < curr_sum:
                    j += 1
                elif iter_sum > curr_sum:
                    k -= 1
                else:
                    return target
                if abs(curr_sum - iter_sum) < abs(diff):
                    diff = curr_sum-iter_sum
        return target-diff