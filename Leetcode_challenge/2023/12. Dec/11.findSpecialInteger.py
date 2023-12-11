'''
1287. Element Appearing More Than 25% In Sorted Array
Easy

1214

56

Add to List

Share
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 105
'''
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        max_count = 1
        max_freq_num = arr[0]
        curr = arr[0]
        curr_count = 1
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                curr_count += 1
            else:
                curr_count = 1
                curr = arr[i]
            if curr_count > max_count:
                max_count = curr_count
                max_freq_num = curr
        
        return max_freq_num