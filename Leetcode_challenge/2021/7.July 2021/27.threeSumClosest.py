'''
3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

 

Constraints:

    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4

'''
# tle
# class Solution:
#     def threeSumClosest(self, nums: [int], target: int) -> int:
#         min_diff = float("inf")
#         res = None
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     sum_nums = nums[i] + nums[j] + nums[k]
#                     if abs(sum_nums - target) < min_diff:
#                         min_diff = abs(sum_nums - target)
#                         res = sum_nums
#                     # print(sum_nums, min_diff, abs(sum_nums - target))
#         return res


class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        min_diff = float("inf")
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums)-1
            while lo < hi:
                three_sum = nums[i] + nums[lo] + nums[hi]
                if abs(three_sum - target) < abs(min_diff):
                    min_diff = three_sum - target
                if three_sum < target:
                    lo += 1
                else:
                    hi -= 1
            if min_diff == 0:
                break
        return target + min_diff

nums = [-1,2,1,-4]
target = 1
# Output: 2

# nums = [1,1,1,0]
# target = -100
# #Output: 2

# nums = [-22,85,-21,-4,-19,91,-54,-50,-4,-27,11,-41,99,32,-4,-70,-42,64,1,30,37,59,-89,6,61,-50,57,-85,-10,18,15,6,75,87,-70,-63,-69,-29,29,84,-35,-27,-91,-47,61,13,20,100,-21,3,-35,63,87,-95,-94,-71,10,21,76,100,-100,-44,-98,-47,63,-41,-82,68,-28,49,5,-50,-83,15,5,-93,94,91,-81,8,-19,6,-19,-34,-69,-69,34,-23,56,-74,19,-31,2,-3,-91,-58,-61,42,-72,-94,-91,-81,-13,-74,8,96,79,-73,14,97,-88,-47,86,61,-31,-63,-83,-12,80,30,65,-14,18,57,-29,-2,41,97,4,-15,79,22,-54,-90,-52,-20,78,-93,-54,94,1,-31,11,0,17,16,-60,90,-39,46,30,-40,-67,-2,-80,-35,58,90,93,50,-5,-38,70,-11,38,-99,-90,-76,69,76,6,96,9,65,-42,-78,-12,-45,41,-90,45,-46,92,-91,-99,74,-43,-34,55,54,45,-76,45]
# # print(len(nums))
# target = 234
# Output: 234

nums = [0,0,0]
target = 1
#Output: 0

sol = Solution()
print(sol.threeSumClosest(nums, target))
