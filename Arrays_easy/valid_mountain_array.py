# def validMountainArray(A: []) -> bool:
# 	if len(A) < 3 or A[1] < A[0]:
# 		return False
# 	i = 2
# 	while i < len(A):
# 		if A[i] > A[i-1]:
# 			i += 1
# 		else:
# 			break
# 	if i == len(A) or A[i] == A[i-1]:
# 		return False
# 	while i < len(A):
# 		if A[i-1] > A[i]:
# 			i += 1
# 		else:
# 			return False
# 	return True

# # A = [2,1]
# # A = [3,5,5]
# # A = [0,3,2,1]
# A = [0,1,2,3,4,5,6,7,8,9]
# print(validMountainArray(A))

# from leetcode copied

def validMountainArray(A: []) -> bool:
    L=len(A)
    i=1
    if L<3:
        return False
    
    while i<L-1 and A[i]>A[i-1]:
        i+=1
    
    while 1<i<L and A[i]<A[i-1]:
        i+=1
    
    if i==L :
        return True
    else:
    	return False

A = [0,1,2,3,4,5,6,7,8,9]
print(validMountainArray(A))
