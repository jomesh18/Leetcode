def thirdMax(nums: []) -> int:
	sorted_nums = sorted(nums)
	max, count = sorted_nums[-1], 0
	for i in range(len(nums)-1, -1, -1):
		if sorted_nums[i] < max:
			max = sorted_nums[i]
			count += 1
			if count == 2:
				break
	if count == 2:
		return max
	else:
		return sorted_nums[-1]

nums = [2, 2, 3, 1]
print(nums)
print(thirdMax(nums))

nums = [1, 2]
print(nums)
print(thirdMax(nums))

nums = [3, 2, 1]
print(nums)
print(thirdMax(nums))


# variety one, not using sort or set

# def thirdMax(self, nums: List[int]) -> int:
#     v = [float('-inf')] * 3
#     for num in nums:
#         if num in v:
#             continue
#         if num > v[0]:   v = [num, v[0], v[1]]
#         elif num > v[1]: v = [v[0], num, v[1]]
#         elif num > v[2]: v = [v[0], v[1], num]
#     return max(nums) if float('-inf') in v else v[2]
