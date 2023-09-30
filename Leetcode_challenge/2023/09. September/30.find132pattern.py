'''
456. 132 Pattern
Medium

6250

346

Add to List

Share
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        min_arr = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            min_arr[i] = min(min_arr[i-1], nums[i])
                   
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_arr[i]:
                while stack and stack[-1] <= min_arr[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
            stack.append(nums[i])
        return False