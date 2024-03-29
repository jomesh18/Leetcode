'''
incomplete
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
a = [2, 3, 1, 1, 5, 3]
n = len(a)
st = [0]*(4*n)
lazy = [0]*(4*n)
marked = [False]*(4*n)

def build(a, tl=0, tr=n-1, pos=1):
	if tl == tr:
		st[pos] = a[tl]
		return
	tm = (tl+tr)//2
	build(a, tl, tm, 2*pos)
	build(a, tm+1, tr, 2*pos+1)
	st[pos] = st[2*pos] + st[2*pos+1]

def add(l, r, value, tl=0, tr=n-1, pos=1):
	if 

def replace(l, r, value, tl=0, tr=n-1, pos=1):


def query(l, r, tl=0, tr=n-1, pos=1):



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

