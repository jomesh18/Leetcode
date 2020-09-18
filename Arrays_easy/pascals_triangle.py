def generate(numRows: int) -> [[]]:
	if numRows == 0:
        return []
	output = [[1]]
	if numRows == 1:
		return output
	output.append([1,1])
	if numRows == 2:
		return output
	for i in range(3, numRows+1):
		temp = [1]
		for j in range(1, i-1):
			temp.append(output[i-2][j]+output[i-2][j-1])
		temp.append(1)
		output.append(temp)
	return output

numRows = 5
print(generate(numRows))
