'''
Permutations

Solution
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
        n = len(nums)
        self.res = []
        all_mask = (1<<n)-1
        def backtrack(curr, curr_mask):
            if curr_mask == all_mask:
                self.res.append(curr[:])
                return
            for i in range(n):
                if not (1<<i & curr_mask):
                    backtrack(curr+[nums[i]], curr_mask | 1<<i)
            
        backtrack([], 0)
        return self.res