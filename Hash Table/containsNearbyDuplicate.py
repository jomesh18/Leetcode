'''
Contains Duplicate II

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
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        duplicate = set()
        if k >= len(nums):
            k = len(nums) - 1
        for i in range(k+1):
            if nums[i] in duplicate:
                return True
            duplicate.add(nums[i])
        print(duplicate)
        i, j = 0, k+1
        while j < len(nums):
            duplicate.remove(nums[i])
            if nums[j] in duplicate:
                return True
            duplicate.add(nums[j])
            i += 1
            j += 1
        return False

#leetcode, fastest
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                prev = d[nums[i]]
                if i-d[nums[i]]<=k:
                    return True
                else:
                    d[nums[i]]=i
            else:
                d[nums[i]]=i

# nums = [1,2,3,1]
# k = 3
# # Output: true

nums = [1,0,1,1]
k = 1
# # Output: true

nums = [1,2,3,1,2,3]
k = 2
# Output: false

nums = [1]
k = 1
# Output: 

sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))
