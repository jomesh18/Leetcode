'''
540. Single Element in a Sorted Array
Medium

7669

123

Add to List

Share
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if mid & 1:
                if mid > 0 and nums[mid] == nums[mid-1]:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                if mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                    lo = mid + 1
                else:
                    hi = mid
        return nums[lo]