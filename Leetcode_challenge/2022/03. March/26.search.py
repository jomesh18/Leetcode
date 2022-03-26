'''
704. Binary Search
Easy

4055

100

Add to List

Share
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
Accepted
741,199
Submissions
1,349,849
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + ((hi-lo)>>1)
            if nums[mid] >= target: hi = mid
            else: lo = mid + 1
        return -1 if (lo == len(nums) or nums[lo] != target) else lo

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = bisect.bisect_left(nums, target)
        return -1 if (ind == len(nums) or nums[ind] != target) else ind