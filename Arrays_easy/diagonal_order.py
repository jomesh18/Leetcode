def findDiagonalOrder(matrix: [[]]) -> []:
	if matrix is None or matrix == [[]] or matrix == []:
		return []
	m, n, l, direction = len(matrix), len(matrix[0]), [], True
	i, j = 0, 0
	while i<m and j<n:
		while i<m and i>=0 and j<n and j>=0:
			l.append(matrix[i][j])
			tail_row = i
			tail_column = j
			if direction:
				i -= 1
				j += 1
			else:
				i += 1
				j -= 1
		if direction:
			if tail_column+1 < n:
				i = tail_row
				j = tail_column + 1
			else:
				i = tail_row + 1
				j = tail_column
		else:
			if tail_row + 1 < m:
				i = tail_row + 1
				j = tail_column
			else:
				i = tail_row
				j = tail_column+1
		direction = not direction
	return l

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(findDiagonalOrder(matrix))

# from leetcode

# def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#     if not matrix: return []
#     m, n = len(matrix), len(matrix[0])
#     if m == 1: return matrix[0]
#     if n == 1: return list(zip(*matrix))[0]
#     starts = [(0,i) for i in range(n)] + [(1+i, n-1) for i in range(m-1)]
#     diags = [[matrix[i+k][j-k] for k in range(min(m-i, j+1))] for i,j in starts]
#     return [v for i in range(len(diags)) for v in diags[i][::i%2*2-1]]

# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# print(findDiagonalOrder(matrix))
