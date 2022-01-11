'''
 Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10

'''

class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# nums = [0]
# Output: [[],[0]]

# nums = [1, 2, 3]
# Output: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

nums = [4,4,4,1,4]
# Output: [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

sol = Solution()
print(sol.subsetsWithDup(nums))
