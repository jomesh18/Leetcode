'''
3Sum

Solution
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {v: i for i, v in enumerate(nums)}
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                key = -(nums[i] + nums[j])
                if key in d and d[key] > i and d[key] > j:
                    # print(i, j, d[key])
                    temp = sorted([nums[i], nums[j], key])
                    res.add((temp[0], temp[1], temp[2]))
        # print(res)
        return [[u[0], u[1], u[2]] for u in res]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or (nums[i] != nums[i-1]):
                target = -nums[i]
                lo = i+1
                hi = len(nums)-1
                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while lo<hi and nums[lo] == nums[lo+1]: lo += 1
                        while hi>lo and nums[hi] == nums[hi-1]: hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < target: lo += 1
                    else: hi -= 1
        return res