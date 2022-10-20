'''
First Missing Positive

Solution
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
'''
# replacing the ith value to its correct position
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] != i+1 and nums[i] < n+1 and nums[nums[i]-1] != nums[i]:
                correct_pos = nums[i] - 1
                temp = nums[correct_pos]
                nums[correct_pos] = nums[i]
                nums[i] = temp
                
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < n+1 and nums[nums[i]-1] != nums[i]:
                correct_pos = nums[i] - 1
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
                
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
