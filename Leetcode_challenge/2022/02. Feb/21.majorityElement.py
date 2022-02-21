'''
169. Majority Element
Easy

8397

313

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
#O(n) time, O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        freq = 0
        maj = 0
        for key in d:
            if d[key] > freq:
                maj = key
                freq = d[key]
        return maj

#O(n) time, O(1) space
import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityCount = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for num in nums if num == candidate) > majorityCount:
                return candidate

#divide and conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = lo + ((hi-lo)>>1)

            left = helper(lo, mid)
            right = helper(mid+1, hi)

            if left == right:
                return left

            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right
        return helper(0, len(nums)-1)

#O(1) space, O(n) time, Bayers Moore Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
