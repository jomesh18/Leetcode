'''

'''
#using array
# class Solution:
#     def findMaxLength(self, nums: [int]) -> int:
#         l = len(nums)
#         arr = [None] * (l*2 + 1)
#         count = 0
#         max_len = 0
#         for i in range(l):
#             if nums[i] == 0:
#                 count -= 1
#             else:
#                 count += 1
#             if count == 0: max_len = i+1
#             if arr[count+l] is not None:
#                 max_len = max(max_len, i-arr[count+l])
#             else:
#                 arr[count+l] = i
#         return max_len

#using hashmap
class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        l = len(nums)
        max_len = 0
        d = {l: -1}
        count = 0
        for i in range(l):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count+l in d:
                max_len = max(max_len, i-d[count+l])
            else:
                d[count+l] = i
        return max_len


nums = [0,0,1,0,0,0,1,1]
# Output: 6

nums = [0,0,1]
# # Output: 2

sol = Solution()
print(sol.findMaxLength(nums))
