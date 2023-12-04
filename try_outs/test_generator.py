import random
n_lo, n_hi = 1, 10**5
q_lo, q_hi = 1, 10**5
e_lo, e_hi = 1, 40

with open('input.txt', 'w') as t:
	n = random.randint(n_lo, n_hi)
	q = random.randint(q_lo, q_hi)
	t.write(str(n)+" "+str(q)+"\n")
	for _ in range(n):
		t.write(str(random.randint(e_lo, e_hi))+" ")
	t.write("\n")

	for _ in range(q):
		typ = random.randint(1, 2)
		x = random.randint(1, n)
		if typ == 1:
			y = random.randint(x, n)
		else:
			y = random.randint(e_lo, e_hi)
		t.write(str(typ)+ " "+str(x)+" "+str(y)+"\n")
