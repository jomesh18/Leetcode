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
#recursive, backtracking
# class Solution:
#     def permute(self, nums: [int]) -> [[int]]:
#         res = []
#         def backtrack(i, temp):
#             if i == len(nums):
#                 res.append(temp)
#                 return 
#             for num in nums:
#                 if num not in temp:
#                     backtrack(i+1, temp+[num])

#         backtrack(0, [])
#         return res

#from leetcode, dfs
class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# nums = [0,1]
# Output: [[0,1],[1,0]]

# nums = [1]
# Output: [[1]]

sol = Solution()
print(sol.permute(nums))
