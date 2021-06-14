'''
Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        if not nums: return 0
        nums.sort() #O(nlogn)
        count, max_c, i = 1, 1, 1
        while i < len(nums):
            while i < len(nums):
                if nums[i] == nums[i-1] + 1:
                    count += 1
                elif nums[i] != nums[i-1]:
                    break
                i += 1
            max_c = max(count, max_c)
            count = 1
            i += 1
        return max_c

#from leetcode, fastest
class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
        
#from leetcode, stefan
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

nums = [100,4,200,1,3,2]
# Output: 4
nums = [0,3,7,2,5,8,4,6,0,1]
# # # Output: 9
nums = []
# # # Output: 0
nums = [0]
# #Output: 1
nums = [0,0]
# #Output: 1
nums = [1,2,0,1]
#Output: 3
s = Solution()
print(s.longestConsecutive(nums))
