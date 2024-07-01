'''
1550. Three Consecutive Odds
Easy

846

73

Add to List

Share
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
'''
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        odd_count = (arr[0] & 1) + (arr[1] & 1) + (arr[2] & 1)
        if odd_count == 3: return True
        for i in range(3, len(arr)):
            if arr[i-3] & 1:
                odd_count -= 1
            if arr[i] & 1:
                odd_count += 1
            if odd_count == 3: return True
        return False