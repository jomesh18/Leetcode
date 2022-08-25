'''
Sort Colors

Solution
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''
#O(1) space, O(n) time, selection sort type
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_end = -1
        one_end = -1
        i = len(nums)-1
        for _ in range(len(nums)):
            if nums[i] == 1:
                one_end += 1
                nums[one_end], nums[i] = nums[i], nums[one_end]
            elif nums[i] == 0:
                zero_end += 1
                one_end = one_end + 1 if one_end >= zero_end else zero_end
                nums[i] = nums[one_end]
                nums[one_end] = nums[zero_end]
                nums[zero_end] = 0
                if nums[one_end] != 1: zero_end
            else:
                i -= 1
        
#O(1) space, O(n) time, easy type
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one = 0, 0
        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
        for i in range(len(nums)):
            if zero:
                nums[i] = 0
                zero -= 1
            elif one:
                nums[i] = 1
                one -= 1
            else:
                nums[i] = 2