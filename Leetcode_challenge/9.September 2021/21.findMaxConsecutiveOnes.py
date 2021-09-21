'''
Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.

'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        max_count, temp_count = 0, 0
        for num in nums:
            if num == 1:
                temp_count += 1
            else:
                max_count = max(max_count, temp_count)
                temp_count = 0
        return max(max_count, temp_count)

nums = [1,1,0,1,1,1]
# # Output: 3

nums = [1,0,1,1,0,1]
# # Output: 2

sol = Solution()
print(sol.findMaxConsecutiveOnes(nums))
