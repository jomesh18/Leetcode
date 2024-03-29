'''
491. Non-decreasing Subsequences
Medium

2191

175

Add to List

Share
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        n = len(nums)    
        def helper(mask, i, added, last_pos):
            # print(mask, i, added)
            if i == n:
                return
                
            if not mask or (last_pos is not None and nums[last_pos] <= nums[i]):
                if added >= 1: self.ans.add(mask | (1 << i))
                helper(mask | (1 << i), i+1, added+1, i)
            helper(mask, i+1, added, last_pos)
        helper(0, 0, 0, None)
        # print(self.ans)
        res = set()
        for mask in self.ans:
            t = []
            for i in range(n):
                if (1<<i) & mask:
                    t.append(nums[i])
            res.add(tuple(t))
        return [list(t) for t in res]


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        n = len(nums)    
        def backtrack(i, curr):
            if i == n:
                if len(curr) >= 2:
                    self.ans.add(tuple(curr))
                return
            if not curr or curr[-1] <= nums[i]:
                backtrack(i+1, curr+[nums[i]])
            backtrack(i+1, curr)
        backtrack(0, [])
        return list(self.ans)


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)    
        for mask in range(1, 1<<n):
            t = [nums[i] for i in range(n) if (mask >> i) & 1]
            if len(t) >= 2 and all(t[i] <= t[i+1] for i in range(len(t)-1)): ans.add(tuple(t))
        return ans
