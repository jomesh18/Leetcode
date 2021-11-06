'''
260. Single Number III
Medium

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
#O(n) time, O(n) space
# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#         s = set()
#         for n in nums:
#             if n in s:
#                 s.remove(n)
#             else:
#                 s.add(n)
#         return list(s)

#O(n) time, O(1) space       
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        xor1, xor2, pos1 = 0, 0, 0
        #xoring all nums to get the two non duplicate nums xor1
        for num in nums:
            xor1 ^= num
        #finding the lsb set bit pos pos1
        for b in range(32):
            if xor1 & 1<<b:
                pos1 = b
                break
        #finding one number with set bit pos pos1
        for num in nums:
            if num & 1<<pos1:
                xor2 ^= num
        return [xor2, xor1^xor2]
        