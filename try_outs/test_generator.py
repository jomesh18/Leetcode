import random
nm_lo, nm_hi = 1, 100000
ai_lo, ai_hi = 0, 10**9

n, m = random.randint(nm_lo, nm_hi), random.randint(nm_lo, nm_hi)
print(str(n)+" "+str(m))
a = [str(random.randint(ai_lo, ai_hi)) for _ in range(n)]
print(" ".join(a))
for _ in range(m):
	t = random.randint(1, 2)
	if t == 1:
		v = random.randint(ai_lo, ai_hi)
		i = random.randint(0, n-1)
		print(str(t)+" "+str(i)+" "+str(v))
	else:
		l = random.randint(0, n-1)
		r = random.randint(l+1, n)
		print(str(t)+" "+str(l)+" "+str(r))
