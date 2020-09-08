# def removeElement(nums: [], val: int):
#     i, index = 0, 0
#     while i < len(nums):
#         while i < len(nums):
#             if nums[i] == val:
#                 i += 1
#             else:
#                 break
#         if i < len(nums):
#             nums[index] = nums[i]
#         else:
#             break
#         index += 1
#         i += 1
#     # print(nums)
#     while index < i:
#         nums.pop()
#         index += 1
#     # print(nums)
#     return len(nums)

# nums = [3,2,2,3]
# val = 3
# print(removeElement(nums, val))

# better logic

def removeElement(nums: [], val: int):
    i = 0
    for num in nums:
        if num != val:
            nums[i] = num
            i += 1
    return i

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))
