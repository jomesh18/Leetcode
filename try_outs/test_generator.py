import random
n_lo, n_hi = 1, 2*10**5
m_lo, m_hi = 1, 2*10**5
r_lo, r_hi = 1, 10**4

with open('input.txt', 'w') as t:
	n = random.randint(n_lo, n_hi)
	m = random.randint(m_lo, m_hi)
	r = random.randint(r_lo, r_hi)
	t.write(str(r)+" "+str(n)+" "+str(m)+"\n")
	for _ in range(n):
		t.write(str(random.randint(0, r-1))+" "+str(random.randint(0, r-1))+"\n")
		t.write(str(random.randint(0, r-1))+" "+str(random.randint(0, r-1))+"\n")
		t.write("\n")

	for _ in range(m):
		l = random.randint(1, n)
		r= random.randint(l, n)
		t.write(str(l)+ " "+str(r)+"\n")