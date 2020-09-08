def sortArrayByParity(A:[]) -> []:
	j = 0
	for i in range(len(A)):
		if A[i]%2 == 0:
			A[i], A[j] = A[j], A[i]
			j += 1
	return A

A = [3,1,2,4]
print(A)
print(sortArrayByParity(A))

# From leetcode, list comprehension
# def sortArrayByParity(self, A: List[int]) -> List[int]:
#     return [i for i in A if i%2 == 0] + [i for i in A if i%2 != 0]

# using lambda function
# def sortArrayByParity(self, A: List[int]) -> List[int]:
#     A.sort(key = lambda x: x % 2)
#     return A
