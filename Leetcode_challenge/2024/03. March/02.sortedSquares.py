'''
977. Squares of a Sorted Array
Easy

8906

223

Add to List

Share
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        np, pp = i-1, i
        for j in range(len(nums)):
            if np >= 0 and pp < len(nums):
                if -nums[np] < nums[pp]:
                    ans[j] = nums[np]*nums[np]
                    np -= 1
                else:
                    ans[j] = nums[pp]*nums[pp]
                    pp += 1
            else:
                if np >= 0:
                    ans[j] = nums[np]*nums[np]
                    np -= 1
                if pp < len(nums):
                    ans[j] = nums[pp]*nums[pp]
                    pp += 1
        return ans