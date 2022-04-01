'''
81. Search in Rotated Sorted Array II
Medium

4258

716

Add to List

Share
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
 

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

Accepted
414,436
Submissions
1,167,088
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.ans = float("inf")
        def helper(i, curr_sum, curr_max, rem):
            if not rem:
                self.ans = min(curr_max, curr_sum+sum(nums[i:]))
                return
            if i == len(nums)-1-rem:
                curr_max = max(curr_max, nums[i:])
                self.ans = min(curr_max, self.ans)
                return
            add_to_curr = helper(i+1, curr_sum+nums[i], max(curr_max, curr_sum+nums[i], rem)
            add_to_next = helper(i+1, nums[i], max(curr_max, nums[i]), rem-1)

        helper(0, 0, 0, m)
        return self.ans
