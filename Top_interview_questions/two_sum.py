'''
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


'''
#brute force

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i and nums[j]+nums[i] == target:
                    return [i, j]

#using dict
class Solution:
	def twoSum(self, nums, target):
	        seen = {}
	        for i, v in enumerate(nums):
	            remaining = target - v
	            if remaining in seen:
	                return [seen[remaining], i]
	            seen[v] = i
	        return []

# same as above
class Solution(object):
	def twoSum(self, nums, target):
		buffer_dictionary = {}
		for i in range(len(nums)):
			if nums[i] in buffer_dictionary:
				return [buffer_dictionary[nums[i]], i] #if a number shows up in the dictionary already that means the 
														#necesarry pair has been iterated on previously
			else: # else is entirely optional
				buffer_dictionary[target - nums[i]] = i 
				# we insert the required number to pair with should it exist later in the list of numbers


nums = [2,7,11,15]
target = 9
# Output: [0,1]
s = Solution()
print(s.twoSum(nums, target))
