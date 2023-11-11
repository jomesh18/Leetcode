'''
https://cses.fi/problemset/task/1735/

CSES - Range Updates and Sums

Time limit: 1.00 s
Memory limit: 512 MB

Your task is to maintain an array of n values and efficiently process the following types of queries:

Increase each value in range [a,b] by x.
Set each value in range [a,b] to x.
Calculate the sum of values in range [a,b].

Input
The first input line has two integers n and q: the array size and the number of queries.
The next line has n values t_1,t_2,\dots,t_n: the initial contents of the array.
Finally, there are q lines describing the queries. The format of each line is one of the following: "1 a b x",  "2 a b x", or "3 a b". 
Output
Print the answer to each sum query.
Constraints

1 \le n, q \le 2 \cdot 10^5
1 \le t_i, x \le 10^6
1 \le a \le b \le n

Example
Input:
6 5
2 3 1 1 5 3
3 3 5
1 2 4 2
3 3 5
2 2 4 5
3 3 5

Output:
7
11
15

'''
class SegmentTree:
	def __init__(self, a):
		self.n = len(a)
		self.t = [0]*(4*self.n)
		self.lazy = [0]*(4*self.n)
		self.build(a, 1, 0, self.n-1)

	def build(self, a, v, tl, tr):
		if tl == tr:
			self.t[v] = a[tl]
		else:
			tm = (tl + tr) // 2
			self.build(a, 2*v, tl, tm)
			self.build(a, 2*v+1, tm+1, tr)
			self.t[v] = self.t[2*v] + self.t[2*v+1]

	def push(v):
		self.t[2*v] += lazy[v]
		self.t[2*v+1] += lazy[v]
		self.lazy[2*v] += lazy[v]
		self.lazy[2*v+1] += lazy[v]
		self.lazy[v] = 0

	def update_range(self, l, r, add):
		self.update_range_util(0, 0, self.n-1, l, r, add)

	def update_range_util(self, v, tl, tr, l, r, add):
		if l > r:
			return 
		if tl == l and tr == r:
			self.t[v] += add
			self.lazy[v] += add
		else:
			self.push(v)
			tm = (tl + tr) // 2
			self.update_range_util(2*v, tl, tm, l, min(tm, r), add)
			self.update_range_util(2*v+1, tm+1, tl, max(l, tm+1), r, add)
			self.t[v] = self.t[2*v]+self.t[2*v+1]

	def query_range(self, l, r):
		return self.query_util(0, 0, self.n-1, l, r)

	def query_util(self, v, tl, tr, l, r):
		if l > r:
			return 0
		if l == tl and r == tr:
			return self.t[v]
		push(v)
		tm = (tl + tr) // 2
		return self.query_util(2*v, tl, tm, l, min(tm, r)) + self.query_util(2*v+1, tm+1, tr, max(l, tm+1), r)

# n, q = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]

# obj = SegmentTree(a)

# for _ in range(q):
# 	inp = [int(i) for i in input().split()]
# 	a, b = inp[1], inp[2]
# 	if inp[0] == 1:
# 		obj.update_range(a, b, inp[3])
# 	elif inp[0] == 2:
# 		obj.set_range(a, b, inp[3])
# 	else:
# 		print(obj.query(a, b))


a = [2, 3, 1, 1, 5, 3]
