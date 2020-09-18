# # recursive approach to correct

# def plusOne(digits: []) -> []:
# 	if digits == []:
# 		digits = [1] + digits
# 		print("1", digits)
# 		return digits
# 	elif digits[-1] != 9:
# 		digits[-1] = digits[-1] + 1
# 		print("2", digits)
# 		return digits
# 	else:
# 		plusOne(digits[:len(digits)-1])
# 		return digits

# # digits = [4,3,2,1]
# digits = [1, 9]
# print(digits)
# print(plusOne(digits))
# print(digits)

# non recursive

def plusOne(digits: []) -> []:
	for i in range(len(digits)-1, -1, -1):
		if digits[i] != 9:
			digits[i] += 1
			break
		else:
			digits[i] = 0
	if digits[0] == 0:
		digits.insert(0, 1)
	return digits

# digits = [4,3,2,1]
digits = [9, 9]
print(digits)
print(plusOne(digits))
