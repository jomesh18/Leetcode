# class Solution:
#     def findMaxConsecutiveOnes(self, nums: [int]) -> int:
#         length = 0
#         i = 0
#         while i<len(nums):
#             if nums[i] == 1:
#                 count = 0
#                 j = i
#                 while j<len(nums) and nums[j] == 1:
#                     count += 1
#                     j += 1
#                 if count > length:
#                     length = count
#                 i = j
#             i += 1
#         return length
#
# obj = Solution()
# nums = [1,1,0,1,1,1]
# print(nums)
# print(obj.findMaxConsecutiveOnes(nums))

# from leetcode
class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        length = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                length = max(length, count)
                count = 0
        # if count > length:
        #     length = count
        return max(length, count)

obj = Solution()
nums = [1,1,0,1,1,1]
print(nums)
print(obj.findMaxConsecutiveOnes(nums))
