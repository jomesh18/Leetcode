'''
665. Non-decreasing Array
Medium

4174

681

Add to List

Share
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 

Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
Accepted
191,970
Submissions
853,124
'''
#len of lis, O(nlogn)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        arr = []
        n = len(nums)
        for i in range(n):
            ind = bisect_right(arr, nums[i])
            if ind == len(arr):
                arr.append(nums[i])
            else:
                arr[ind] = nums[i]
        return n-1 <= len(arr)

#O(n)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if cnt: return False
                cnt += 1
                if i-2 >= 0 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
        return True