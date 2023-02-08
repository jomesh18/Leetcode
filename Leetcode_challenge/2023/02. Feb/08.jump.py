'''
45. Jump Game II
Medium

10941

380

Add to List

Share
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0
        while i < len(nums)-1:
            count += 1
            nex = i
            for k in range(i+1, i+nums[i]+1):
                if k == len(nums)-1: return count
                if nums[k]+k >= nex:
                    nex = nums[k]+k
                    i = k
        return count