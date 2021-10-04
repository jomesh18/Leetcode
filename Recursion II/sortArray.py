'''
Sort an Array

Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

 

Constraints:

    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
'''
#top down merge sort
class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        if len(nums) <= 1: return nums
        pivot = len(nums)//2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left, right)

    def merge(self, left, right):
        left_index, right_index = 0, 0
        res = []
        while left_index<len(left) and right_index<len(right):
            if left[left_index] < right[right_index]:
                res.append(left[left_index])
                left_index += 1
            else:
                res.append(right[right_index])
                right_index += 1
        res.extend(left[left_index:])
        res.extend(right[right_index:])

        return res

# Bottom-up Approach merge sort
class Solution:
    def sortArray(self, nums: [int]) -> [int]:

        
nums = [5,2,3,1]
# # Output: [1,2,3,5]

# nums = [5,1,1,2,0,0]
# # Output: [0,0,1,1,2,5]

sol = Solution()
print(sol.sortArray(nums))
