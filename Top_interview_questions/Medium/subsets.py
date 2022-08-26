'''
Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''
#iterative
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            t = []
            for l in res:
                t.append(l+[n])
            res.extend(t)
        return res

#backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        n = len(nums)
        
        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                self.res.append(curr[:])
                return
            for i in range(first, n):
                backtrack(i+1, curr+[nums[i]])
            
        for k in range(n+1):
            backtrack()
        return self.res

#backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        n = len(nums)
        
        def backtrack(first=0, curr=[]):
            self.res.append(curr[:])
            for i in range(first, n):
                backtrack(i+1, curr+[nums[i]])
            
        backtrack(0, [])
        return self.res

#mask
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(2**n, 2**(n+1)):
            mask = bin(i)[3:]
            res.append([nums[i] for i in range(n) if mask[i] == '1'])
        return res