'''
Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

 

Constraints:

    1 <= nums.length <= 1000
    -231 <= nums[i] <= 231 - 1
    nums[i] != nums[i + 1] for all valid i.

'''

class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        # leng = len(nums)
        # l, r = 0, len(nums)
        # nums.append(float("-inf"))
        # while l<r:
        #     mid = (l+r)//2
        #     if nums[(mid-1)] < nums[mid] and nums[(mid+1)%leng] < nums[mid]:
        #         return mid
        #     elif nums[mid] < nums[(mid+1)%leng]:
        #         l = mid + 1
        #     else:
        #         r = mid

        l, r = 0, len(nums)
        nums.append(float("-inf"))
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] > nums[mid-1]:
                l = mid
            else:
                r = mid
        # return l%len(nums)

nums = [1,2,3,1]
# Output: 2

nums = [1,2,1,3,5,6,4]
# # Output: 5

nums = [1]
# Output: 0

nums = [2,1]
# Output: 0

s = Solution()
print(s.findPeakElement(nums))
