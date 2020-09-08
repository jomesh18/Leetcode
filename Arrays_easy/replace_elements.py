# # using a function to find greatest

# def replaceElements(arr: [int]) -> [int]:
# 	index, i = 0, 0
# 	while index < len(arr)-1:
# 		i = index + 1 + find_greatest(arr[index+1:])
# 		for j in range(index, i):
# 			arr[j] = arr[i]
# 			index += 1
# 	arr[-1] = -1
# 	return arr

# def find_greatest(arr):
# 	greatest = 0
# 	for i in range(len(arr)):
# 		if arr[i] > arr[greatest]:
# 			greatest = i
# 	return greatest

# arr = [17,18,5,4,6,1]
# replaceElements(arr)
# print(arr)

# not using a function to find greatest

def replaceElements(arr: [int]) -> [int]:
	index = 0
	while index < len(arr)-1:
		greatest = index + 1
		for k in range(index+1, len(arr)):
			if arr[k] > arr[greatest]:
				greatest = k
		for j in range(index, greatest):
			arr[j] = arr[greatest]
			index += 1
	arr[-1] = -1
	return arr

arr = [17,18,5,4,6,1]
replaceElements(arr)
print(arr)
