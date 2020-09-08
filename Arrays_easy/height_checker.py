def heightChecker(heights: []) -> int:
	sorted_h = sorted(heights)
	counter = 0
	for i in zip(sorted_h, heights):
		if i[0] != i[1]:
			counter += 1
	return counter

heights = [5,1,2,3,4]
print(heightChecker(heights))
