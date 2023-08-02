'''
46. Permutations
Medium

16854

267

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def helper(mask, curr):
            if mask == (1<<n)-1:
                ans.append(curr[:])
                return
            for i in range(n):
                if not ((mask>>i) & 1): 
                    helper(mask | (1<<i), curr+[nums[i]])
        helper(0, [])
        return ans
            