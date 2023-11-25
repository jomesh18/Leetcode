n, m = [int(i) for i in input().split()]
a = [0]*n

st = [0]*(4*n)

def query(i, tl=0, tr=n-1, pos=1):
	if tl == tr:
		return st[pos]
	tm = (tl+tr)//2
	if i <= tm:
		return query(i, tl, tm, 2*pos)
	else:
		return query(i, tm+1, tr, 2*pos+1)

def update(i, val, tl=0, tr=n-1, pos=1):
	if tl == tr:
		st[pos] += val
	else:
		tm = (tl+tr)//2
		if i <= tm:
			update(i, val, tl, tm, 2*pos)
		else:
			update(i, val, tm+1, tr, 2*pos+1)

for _ in range(m):
	ins = [int(i) for i in input().split()]
	if ins[0] == 1:
		for k in range(ins[1], ins[2]):
			update(k, ins[3])
	else:
		print(query(ins[1]))