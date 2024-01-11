import random

Q = []
n_lo, n_hi = 4, 6
q_lo, q_hi = 5, 8
e_hi = 9
e_lo = -9

n = random.randint(n_lo, n_hi)
q = random.randint(q_lo, q_hi)
Q.append(str(n)+" "+str(q))

for _ in range(q):
	# typ = random.randint(1, 2)
	# if typ == 1:
		l = random.randint(0, n-1)
		r = random.randint(l+1, n)
		e = random.randint(e_lo, e_hi)
		Q.append(str(l)+" "+str(r)+" "+str(e))
	# else:
	# 	l = random.randint(0, n-1)
	# 	r = random.randint(l+1, n)
	# 	Q.append(str(typ)+ " "+str(l)+" "+str(r))

print(*Q, sep="\n")
