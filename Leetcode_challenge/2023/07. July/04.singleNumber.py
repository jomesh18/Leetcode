'''
137. Single Number II
Medium

6233

574

Add to List

Share
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            s = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)
                s += (num>>i) & 1
            s %= 3
            ans |= (s<<i)
        if ans >= 2**31:
            ans -= 2**32
        return ans



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)
        return ones