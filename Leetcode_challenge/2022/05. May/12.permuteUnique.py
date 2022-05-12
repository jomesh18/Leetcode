'''
47. Permutations II
Medium

5207

95

Add to List

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
Accepted
623,080
Submissions
1,139,117
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        count = Counter(nums)
        
        def dfs(t, count):
            if len(t) == len(nums):
                res.append(t[:])
                return
            for key in count:
                if count[key] > 0:
                    count[key] -= 1
                    dfs(t+[key], count)
                    count[key] += 1
        dfs([], count)
        return res
