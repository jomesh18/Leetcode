'''
3152. Special Array II
Medium

440

33

Add to List

Share
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that subarray nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
'''
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix_sum = [0]*(n+1)
        for i in range(1, n):
            prefix_sum[i+1] = prefix_sum[i] + (1 if ((nums[i] & 1) ^ (nums[i-1] & 1)) else 0)
        # print(prefix_sum)
        ans = [False]*len(queries)
        for i, (l, r) in enumerate(queries):
            if l == r:
                ans[i] = True
                continue
            if l == 0:
                if prefix_sum[r+1] == r-l:
                    ans[i] = True
                    continue
            else:
                curr = prefix_sum[r+1] - prefix_sum[l]
                if ((nums[l] & 1) ^ (nums[l-1] & 1)):
                    curr -= 1
                if curr == r-l:
                    ans[i] = True
        return ans