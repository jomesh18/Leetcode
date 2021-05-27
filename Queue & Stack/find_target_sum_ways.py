'''
Target Sum

Solution
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''
# time limit exceeded, recursive way
# class Solution:
#     def findTargetSumWays(self, nums: [int], target: int) -> int:
#         self.count = 0 # this is the count of the number of ways to get the target
#         def helper(nums, target, ans):
#             if not nums:    # if we reached the last number, check if it is equal to target and increment the count
#                 if ans == target:
#                     self.count += 1
#                 return
#             helper(nums[1:], target, ans+nums[0])   # recursively go with +
#             helper(nums[1:], target, ans-nums[0])   # recursively go with -
#         helper(nums, target, 0)
#         return self.count

# time limit exceeded, iterative:
# class Solution:
#     def findTargetSumWays(self, nums: [int], target: int) -> int:
#         l = [0]
#         for i in nums:
#             l = [j+i for j in l]
#             k = [-i for i in l]
#             l = l+k
#         return [i==target for i in l].count(True)

#recursive with memoization, from leetcode
# class Solution:
#     def findTargetSumWays(self, nums, S):
#         index = len(nums) - 1
#         curr_sum = 0
#         self.memo = {}
#         return self.dp(nums, S, index, curr_sum)
        
#     def dp(self, nums, target, index, curr_sum):
#         if (index, curr_sum) in self.memo:
#             return self.memo[(index, curr_sum)]
        
#         if index < 0 and curr_sum == target:
#             return 1
#         if index < 0:
#             return 0 
        
#         positive = self.dp(nums, target, index-1, curr_sum + nums[index])
#         negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
        
#         self.memo[(index, curr_sum)] = positive + negative
#         return self.memo[(index, curr_sum)]




# memoization, my try
# class Solution:
#     def findTargetSumWays(self, nums: [int], target: int) -> int:
#         memo = {}
#         def helper(nums, target, index, s):
#             if (index, s) in memo:
#                 return memo[(index, s)]
#             if index < 0 and s == target:
#                 return 1
#             elif index < 0:
#                 return 0
#             positive = helper(nums, target, index-1, s+nums[index])
#             negative = helper(nums, target, index-1, s-nums[index])
#             memo[(index, s)] = positive + negative
#             return memo[(index, s)]

#         return helper(nums, target, len(nums)-1, 0)

#from leetcode, using two dictionaries
# from collections import defaultdict

# class Solution:
#     def findTargetSumWays(self, nums, S):
#         count = defaultdict(int)
#         count[0] = 1
#         for x in nums:
#             step = defaultdict(int)
#             for y in count:
#                 step[y + x] += count[y]
#                 step[y - x] += count[y]
#             count = step

#         return count[S]
    #below is same, but more understandable
    # def findTargetSumWays(self, nums: [int], S: int) -> int:
    #     counter = {0: 1}
    #     for x in nums:
    #         tmp = {}
    #         for val, count in counter.items():
    #             s = val + x
    #             tmp[s] = tmp.get(s, 0) + count

    #             s = val - x
    #             tmp[s] = tmp.get(s, 0) + count
    #         counter = tmp
    #         print(counter, len(counter))

    #     return counter.get(S, 0)


#above, my try
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        d = defaultdict(int)
        d = {0: 1}
        for num in nums:
            temp = defaultdict(int)
            for s in d:
                temp[s+num] += d[s]
                temp[s-num] += d[s]
            d = temp
        return d.get(target, 0)

# nums = [1,1,1,1,1]
# target = 3
# Output: 5
# nums = [1]
# target = 1
# # Output: 1
# nums = [35,25,24,23,2,47,39,22,3,7,11,26,6,30,5,34,10,43,41,28]
# print(len(nums))
# target = 49
# Output: 6266
nums = [26,33,25,41,15,46,36,11,29,18,17,26,28,11,39,4,19,13,40,8]
print(len(nums))
target = 5
Output: 6747
# nums = [0, 0]
# target = 0
# Output: 4

s = Solution()
print(s.findTargetSumWays(nums, target))
