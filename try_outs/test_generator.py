import random
nm_lo, nm_hi = 1, 10
ai_lo, ai_hi = -10**9, 10**9

with open('input.txt', 'w') as t:
	n, m = random.randint(nm_lo, nm_hi), random.randint(nm_lo, nm_hi)
	t.write(str(n)+" "+str(m)+"\n")
	a = [str(random.randint(ai_lo, ai_hi)) for _ in range(n)]
	t.write(" ".join(a)+"\n")
	for _ in range(m):
		i = random.randint(0, n-1)
		v = random.randint(-10**9, 10**9)
		t.write(str(i)+ " "+str(v)+"\n")
