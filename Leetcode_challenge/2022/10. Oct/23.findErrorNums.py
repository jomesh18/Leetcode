'''
645. Set Mismatch
Easy

3231

753

Add to List

Share
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # s = set(i+1 for i in range(len(nums)))
        s = set()
        ans = []
        for num in nums:
            if num in s:
                ans.append(num)
            s.add(num)
        for i in range(1, len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans

#o(1) space
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans

# using xor
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor, xor1, xor2 = 0, 0, 0
        for i in range(len(nums)):
            xor ^= (i+1)
            xor ^= (nums[i])
        rightmost = xor & ~(xor-1)
        for num in nums:
            if num & rightmost:
                xor1 ^= num
            else:
                xor2 ^= num
        for i in range(1, len(nums)+1):
            if i & rightmost:
                xor1 ^= i
            else:
                xor2 ^= i
        for num in nums:
            if num == xor1:
                return [xor1, xor2]
        return [xor2, xor1]