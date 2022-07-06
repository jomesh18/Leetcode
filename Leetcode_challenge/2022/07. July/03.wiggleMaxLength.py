'''
376. Wiggle Subsequence
Medium

4087

132

Add to List

Share
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.

 

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
 

Follow up: Could you solve this in O(n) time?
'''
#dp O(n) time, O(n) space
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [1] + [0]*(n-1)
        down = [1] + [0]*(n-1)
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                up[i] = up[i-1]
                down[i] = up[i-1] + 1
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[-1], down[-1])

#dp O(n) time, O(1) space
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = 1
        down = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)

#greedy approach, O(n) time, O(1) space
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxlen = 1
        sign = 0
        for i in range(1, n):
            if nums[i] > nums[i-1] and sign != 1: #valley
                sign = 1
                maxlen += 1
            elif nums[i] < nums[i-1] and sign != -1: #peak
                sign = -1
                maxlen += 1
        return maxlen