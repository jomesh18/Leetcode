# def checkIfExist(arr: []) -> bool:
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if (arr[i] == 2*arr[j] or arr[j] == 2*arr[i]):
#                 if i != j:
#                     return True
#     return False

# # arr = [10, 2, 5, 3]
# # arr = [7,1,14,11]
# arr = [3,1,7,11]
# print(checkIfExist(arr))

# better one O(n)

def checkIfExist(arr: []) -> bool:
	d = set()
	for i in arr:
		if i*2 in d or i/2 in d:
			return True
		d.add(i)
	return False

# arr = [10, 2, 5, 3]
arr = [7,1,14,11]
# arr = [3,1,7,11]
print(checkIfExist(arr))
