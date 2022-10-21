'''
219. Contains Duplicate II
Easy

3628

2260

Add to List

Share
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        d = {}
        k += 1
        for i in range(min(k, len(nums))):
            if nums[i] in d:
                return True
            d[nums[i]] = i
        for i in range(k, len(nums)):
            del d[nums[i-k]]
            if nums[i] in d:
                return True
            d[nums[i]] = i
        return False