def find_numbers(nums):
	count = 0
	for num in nums:
		digit_count = 0
		while num != 0:
			digit_count += 1
			num = int(num/10)
		if (digit_count % 2 == 0):
			count += 1
	return count
	
print(find_numbers([555,901,482,1771]))
