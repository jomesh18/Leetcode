'''
260. Single Number III
Medium

5878

245

Add to List

Share
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor1 = 0
        for num in nums:
            xor1 ^= num 
        l_set_b = 0
        for i in range(32):
            if (1<<i) & xor1:
                l_set_b = i
                break
        xor2 = 0
        for num in nums:
            if num & (1<<l_set_b):
                xor2 ^= num
        return [xor1 ^ xor2, xor2]
    