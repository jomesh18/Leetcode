'''
1043. Partition Array for Maximum Sum
Medium

3929

284

Add to List

Share
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
'''
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}
        def helper(i, start, prev_max_pos):
            if i == len(arr):
                return (i-start)*arr[prev_max_pos]
            if (i, start, prev_max_pos) in memo: return memo[(i, start, prev_max_pos)]
            ans = arr[prev_max_pos]*(i-start) + helper(i+1, i, i) #starting new
            if i-start+1 <= k: # adding to old
                ans = max(ans, helper(i+1, start, i if arr[i] > arr[prev_max_pos] else prev_max_pos))
            memo[(i, start, prev_max_pos)] = ans
            return ans
        return helper(0, 0, 0)