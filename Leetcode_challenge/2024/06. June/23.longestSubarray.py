'''
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium

4002

187

Add to List

Share
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109
'''
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, min_heap, max_heap, ans = 0, [], [], 0
        for r, num in enumerate(nums):
            heappush(min_heap, (num, r))
            heappush(max_heap, (-num, r))
            while -max_heap[0][0] - min_heap[0][0] > limit or max_heap[0][1] < l or min_heap[0][1] < l:
                if max_heap[0][1] < min_heap[0][1]:
                    l = max(l, max_heap[0][1]+1)
                    heappop(max_heap)
                else:
                    l = max(l, min_heap[0][1]+1)
                    heappop(min_heap)
            ans = max(ans, r-l+1)
        return ans
