def moveZeroes(nums: []) -> None:
	new_index = 0
	for old_index in range(len(nums)):
		if nums[old_index] != 0:
			nums[new_index] = nums[old_index]
			new_index += 1
	for _ in range(new_index, len(nums)):
		nums[new_index] = 0
		new_index += 1

nums = [0,1,0,3,12]
print(nums)
moveZeroes(nums)
print(nums)
