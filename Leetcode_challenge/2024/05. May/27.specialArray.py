'''
1608. Special Array With X Elements Greater Than or Equal X
Easy

1815

317

Add to List

Share
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
Example 3:

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        lo, hi = 0, max(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_count = sum(1 for num in nums if num >= mid)
            if mid_count == mid:
                return mid
            elif mid_count > mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0]*(n+1)
        for num in nums:
            freq[min(n, num)] += 1
        count = 0
        for i in range(n, 0, -1):
            count += freq[i]
            if count == i:
                return i
        return -1