def max_profit(prices):
	min = prices[0]
	profits = []
	for i in range(1, len(prices)):
		if prices[i] < min:
			min = prices[i]
		elif prices[i] > min:
			profit += (prices[i]-min)
			if i<len(prices)-1:
				min = prices[i+1]
	return profit

print(max_profit([1, 4, 2, 7, 6, 5]))
print(max_profit([7,1,5,3,6,4]))
print(max_profit([1,2,3,4,5]))
print(max_profit([7,6,4,3,1]))
