# def removeDuplicates(nums: []) -> int:
#     index, i = 0, 1
#     while i < len(nums):
#         if nums[i] != nums[index]:
#             nums[index+1] = nums[i]
#             index += 1
#             i += 1
#         else:
#             i += 1
#     while index < i-1:
#         nums.pop()
#         index += 1

# nums = [1,1,2]
# print(nums)
# removeDuplicates(nums)
# print(nums)

# using for loop

def removeDuplicates(nums: []) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]
    nums[:] = nums[:index+1]

nums = [1,1,2]
print(nums)
removeDuplicates(nums)
print(nums)
