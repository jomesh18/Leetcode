import random
n_lo, n_hi = 1, 10
m_lo, m_hi = 1, 10**5

with open('input.txt', 'w') as t:
	n, m = random.randint(n_lo, n_hi), random.randint(m_lo, m_hi)
	t.write(str(n)+" "+str(m)+"\n")
	for _ in range(m):
		type = random.randint(1, 2)
		if type == 1:
			l = random.randint(0, n-1)
			r = random.randint(l+1, n)
			v= random.randint(0, 10**9)
			t.write(str(type)+ ' '+str(l)+ " "+str(r)+ " "+str(v)+"\n")
		else:
			i = random.randint(0, n-1)
			t.write(str(type)+" "+str(i)+"\n")