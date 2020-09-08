# # naive approach, finding left and right every time
# def pivotIndex(nums: ()) -> int:
# 	for i in range(0, len(nums)):
# 		left, right = 0, 0
# 		for j in range(0, i):
# 			left += nums[j]
# 		for j in range(i+1, len(nums)):
# 			right += nums[j]
# 		if left == right:
# 			return i
# 	return -1

# # nums = [1,7,3,6,5,6]
# # nums = [1, 2, 1]
# # nums = [-1,-1,-1,0,1,1]
# nums = [-1,-1,0,1,1,5]
# print(nums)
# print(pivotIndex(nums))

# better approach, finding left and right and adding/subtracting to/from it

def pivotIndex(nums: ()) -> int:
	if nums == []:
		return -1
	left, right = 0, 0
	for i in range(1, len(nums)):
		right += nums[i]
	if left == right:
		return 0
	for i in range(1, len(nums)):
		left += nums[i-1]
		right -= nums[i]
		if left == right:
			return i
	return -1

nums = [1,7,3,6,5,6]
# nums = [1, 2, 1]
# nums = [-1,-1,-1,0,1,1]
# nums = [-1,-1,0,1,1,5]
print(nums)
print(pivotIndex(nums))
