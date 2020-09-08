# # Using a third list

# def merge(nums1, m, nums2, n):
# 	i, j, k = 0, 0, 0
# 	nums3 = []
# 	while k < m+n:
# 		if i >= m:
# 			nums3.extend(nums2[j:])
# 			break
# 		if j >= n:
# 			nums3.extend(nums1[i:m])
# 			break
# 		if nums1[i] < nums2[j]:
# 			nums3.append(nums1[i])
# 			i += 1
# 			k += 1
# 		else:
# 			nums3.append(nums2[j])
# 			j += 1
# 			k += 1
# 	nums1[:] = nums3[:]
# 	# print(nums1)

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# merge(nums1, m, nums2, n)
# print(nums1)

# not using a third list, using insert

# def merge(nums1, m, nums2, n):
# 	if m == 0:
# 		nums1[:] = nums2[:]
# 		return
# 	i, j, count = 0, 0, 0
# 	while i < m+n:
# 		if count >= m:
# 			nums1[i:] = nums2[j:]
# 			break
# 		if j >= n:
# 			break
# 		if nums1[i] > nums2[j]:
# 			nums1.insert(i, nums2[j])
# 			nums1.pop()
# 			j += 1
# 		else:
# 			count += 1
# 		i += 1
	
# # nums1 = [1,2,3,0,0,0]
# # m = 3
# # nums2 = [2,5,6]
# # n = 3
# # merge(nums1, m, nums2, n)
# # print(nums1)
# nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# m = 1
# nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
# n = 90
# print(len(nums1), len(nums2))
# print(nums1)
# print(nums2)
# merge(nums1, m, nums2, n)
# print(nums1)

# not using third list, not using insert

def merge(nums1, m, nums2, n):
	if m == 0:
		nums1[:] = nums2[:]
		return
	elif n == 0:
		return
	i, j, count, q = 0, 0, 0, []
	while i < m:
		if nums1[i] <= nums2[j]:
			i += 1
			count += 1
		else:
			break
	if i == m:
		nums1[i:] = nums2[j:]
	else:
		q.append(nums1[i])
		elem = q.pop(0)
		while i < m+n:
			if count == m:
				nums1[i:] = nums2[j:]
				break
			elif j == n:
				nums1[i] = elem
				i += 1
				count += 1
				while count < m:
					q.append(nums1[i])
					nums1[i] = q.pop(0)
					i += 1
					count += 1
			elif elem < nums2[j]:
				nums1[i] = elem
				i += 1
				q.append(nums1[i])
				elem = q.pop(0)
				count += 1
			else:
				nums1[i] = nums2[j]
				j += 1
				i += 1
				q.append(nums1[i])

# nums1 = [2,0]
# m = 1
# nums2 = [1]
# n = 1
# nums1 = [4,5,6,0,0,0]
# m = 3
# nums2 = [1,2,3]
# n = 3
# nums1 = [1,2,4,5,6,0]
# m = 5
# nums2 = [3]
# n = 1
# merge(nums1, m, nums2, n)
# print(nums1)

# nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# m = 1
# nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
# n = 90
# print(len(nums1), len(nums2))
# print(nums1)
# print(nums2)
# merge(nums1, m, nums2, n)
# print(nums1)