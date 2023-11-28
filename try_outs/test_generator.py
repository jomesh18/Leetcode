import random
n_lo, n_hi = 1, 5
m_lo, m_hi = 1, 5
e_lo, e_hi = 1, 5

with open('input.txt', 'w') as t:
	n = random.randint(n_lo, n_hi)
	t.write(str(n)+"\n")
	a = [str(random.randint(e_lo, e_hi)) for _ in range(n)]
	t.write(" ".join(a)+"\n")
	m = random.randint(m_lo, m_hi)
	t.write(str(m)+"\n")
	for _ in range(m):
		type = random.randint(0, 1)
		if type == 0:
			i = random.randint(1, n)
			v= random.randint(e_lo, e_hi)
			t.write(str(type)+ ' '+str(i)+ " "+str(v)+"\n")
		else:
			l = random.randint(1, n)
			r= random.randint(l, n)
			t.write(str(type)+ ' '+str(l)+ " "+str(r)+"\n")