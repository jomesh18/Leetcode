'''
525. Contiguous Array
Medium

4988

214

Add to List

Share
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
Accepted
249,934
Submissions
542,242
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        max_len = 0
        d = {l: -1}
        count = 0
        for i in range(l):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count+l in d:
                max_len = max(max_len, i-d[count+l])
            else:
                d[count+l] = i
        return max_len