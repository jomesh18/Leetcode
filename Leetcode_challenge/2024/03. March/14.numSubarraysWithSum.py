'''
930. Binary Subarrays With Sum
Medium

3155

88

Add to List

Share
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
'''
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curr = 0
        ans = 0
        d = {}
        for num in nums:
            curr += num
            if curr == goal:
                ans += 1
            if curr - goal in d:
                ans += d[curr-goal]
            d[curr] = d.get(curr, 0) + 1
        return ans