# using list.sort()

# def sortedSquares(A: []) -> []:
# 	b = [i*i for i in A]
# 	b.sort()
# 	return b

# A = [-4,-1,0,3,10]
# print(A)
# print(sortedSquares(A))

# Using lambda

# def sortedSquares(A: []) -> []:
# 	A.sort(key = lambda x: abs(x))
# 	return [i*i for i in A]

# A = [-4,-1,0,3,10]
# print(A)
# print(sortedSquares(A))

# using sorted(list)

def sortedSquares(A: []) -> []:
	return sorted(x**2 for x in A)

A = [-4,-1,0,3,10]
print(A)
print(sortedSquares(A))
