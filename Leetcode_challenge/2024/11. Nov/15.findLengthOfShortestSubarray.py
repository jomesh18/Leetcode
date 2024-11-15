'''
1574. Shortest Subarray to be Removed to Make Array Sorted
Solved
Medium
Topics
Companies
Hint
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 

Constraints:

1 <= arr.length <= 105
0 <= arr[i] <= 109
'''
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        inc_from_start_last = n-1
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                inc_from_start_last = i-1
                break
        if inc_from_start_last == n-1: return 0
        dec_from_end_last = 0
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                dec_from_end_last = i+1
                break
        # print(inc_from_start_last, dec_from_end_last)
        def helper(i, j):
            if i == -1:
                return n-j
            if j == n:
                return i+1
            if arr[i] <= arr[j]:
                return i+1+n-j
            return max(helper(i-1, j), helper(i, j+1))
        return n-helper(inc_from_start_last, dec_from_end_last)