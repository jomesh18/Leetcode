'''
448. Find All Numbers Disappeared in an Array
Easy

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n

 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
Accepted
462,153
Submissions
800,993
'''
class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        for num in nums:
            num = abs(num)
            nums[num-1] = -abs(nums[num-1])
        return [i+1 for i, num in enumerate(nums) if num>0]

nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# nums = [1,1]
# Output: [2]

sol = Solution()
print(sol.findDisappearedNumbers(nums))
