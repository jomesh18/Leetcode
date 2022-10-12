'''
976. Largest Perimeter Triangle
Easy

1742

243

Add to List

Share
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
Accepted
130,204
Submissions
243,295
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3, -1, -1):
            if nums[i]+nums[i+1] > nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0