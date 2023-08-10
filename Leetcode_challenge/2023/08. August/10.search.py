'''
81. Search in Rotated Sorted Array II
Medium

7007

896

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
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def exists_in_first(nums, start, elem):
            return elem >= nums[start]
        
        def is_bsearch_useful(nums, start, elem):
            return elem != nums[start]
        
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target: return True
            if not is_bsearch_useful(nums, lo, nums[mid]):
                lo += 1
                continue
            curr_pos = exists_in_first(nums, lo, nums[mid])
            t_pos = exists_in_first(nums, lo, target)
            if (t_pos ^ curr_pos):
                if curr_pos:
                    lo = mid+1
                else:
                    hi = mid - 1
            else:
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False