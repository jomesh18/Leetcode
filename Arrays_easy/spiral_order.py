def spiralOrder(matrix: [[]]) -> []:
	if matrix is None or matrix == [] or matrix == [[]]:
        return []
	m, n, l = len(matrix), len(matrix[0]), []
	tr, rc, lc, br = 0, n-1, 0, m-1
	i, j = 0, 0
	while br > tr and rc > lc:
		print(tr, rc, lc, br)
		while j<=rc:
			l.append(matrix[i][j])
			print(i, j)
			j += 1
		j -= 1
		i += 1
		while i <= br:
			l.append(matrix[i][j])
			print(i, j)
			i += 1
		i -= 1
		j -= 1
		while j >= lc:
			l.append(matrix[i][j])
			print(i, j)
			j -= 1
		j += 1
		i -= 1
		while i > tr:
			l.append(matrix[i][j])
			print(i, j)
			i -= 1
		i += 1
		j += 1
		tr += 1
		rc -= 1
		lc += 1
		br -= 1
	if lc == rc == tr == br:
		l.append(matrix[tr][lc])
	elif br == tr:
		l.extend(matrix[br][lc:rc+1])
	elif rc == lc:
		while br>=tr:
			l.append(matrix[tr][rc])
			tr += 1
	return l

# matrix = [[6, 5, 8, 7, 2, 6],
#        [2, 9, 8, 4, 9, 7],
#        [1, 6, 4, 0, 4, 9],
#        [9, 9, 3, 5, 6, 9],
#        [8, 3, 0, 9, 0, 1],
#        [9, 9, 3, 9, 3, 5]]
# print(spiralOrder(matrix))

matrix = [[0, 1, 5, 4, 0, 2],
       [6, 6, 0, 3, 3, 8],
       [8, 6, 6, 2, 0, 6],
       [2, 4, 4, 9, 6, 6],
       [6, 1, 0, 6, 5, 6]]
print(spiralOrder(matrix))
