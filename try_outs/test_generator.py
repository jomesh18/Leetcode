import random
n_lo, n_hi = 1, 1000
q_lo, q_hi = 1, 1000
e_hi = 1000

with open('input.txt', 'w') as t:
	n = random.randint(n_lo, n_hi)
	q = random.randint(q_lo, q_hi)
	t.write(str(n)+" "+str(q)+"\n")

	for _ in range(q):
		typ = random.randint(1, 2)
		if typ == 1:
			l = random.randint(0, n-1)
			r = random.randint(l+1, n)
			p = random.randint(0, e_hi)
			t.write(str(typ)+ " "+str(l)+" "+str(r)+" "+str(p)+"\n")
		else:
			l = random.randint(0, n-1)
			r = random.randint(l+1, n)
			t.write(str(typ)+ " "+str(l)+" "+str(r)+"\n")
