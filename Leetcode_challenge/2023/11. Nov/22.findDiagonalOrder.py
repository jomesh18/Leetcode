'''
1424. Diagonal Traverse II
Solved
Medium
Topics
Companies
Hint
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

 

Example 1:


Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:


Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105
'''
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = defaultdict(list)
        max_c_len = 0
        for i in range(n):
            max_c_len = max(max_c_len, len(nums[i]))
            for j in range(len(nums[i])):
                ans[i+j].append(nums[i][j])
        ret = []
        for s in range(max_c_len+n-1):
            if s in ans:
                ret.extend(ans[s][::-1])
        return ret