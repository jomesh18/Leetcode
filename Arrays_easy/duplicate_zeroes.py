def duplicate_zeroes(arr):
	q = []
	i = 0
	while i<len(arr):
		if arr[i] != 0:
			i += 1
		else:
			break
	i += 1
	if i < len(arr):
		q.append(arr[i])
		arr[i] = 0
		i += 1
	while i<len(arr):
		q.append(arr[i])
		elem = q.pop(0)
		if elem != 0:
			arr[i] = elem
		else:
			arr[i] = 0
			i += 1
			if i<len(arr):
				q.append(arr[i])
				arr[i] = 0
		i += 1

arr = [1, 2, 3, 4]
# arr = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
print(arr)
duplicate_zeroes(arr)
print(arr)
