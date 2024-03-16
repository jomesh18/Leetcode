'''
525. Contiguous Array
Medium

7264

319

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
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        d = {0: -1}
        ans = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in d:
                ans = max(ans, i-d[count])
            else:
                d[count] = i
        return ans