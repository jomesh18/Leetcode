'''
862. Shortest Subarray with Sum at Least K
Hard

4885

135

Add to List

Share
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        curr = 0
        ans = float('inf')
        pq = []
        
        for i in range(len(nums)):
            curr += nums[i]
            if curr >= k:
                ans = min(ans, i+1)
            while pq and curr-pq[0][0] >= k:
                old_sum, l = heappop(pq)
                ans = min(ans, i-l)
            heappush(pq, (curr, i))

        return ans if ans != float('inf') else -1