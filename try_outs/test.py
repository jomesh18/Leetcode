import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
MOD = 10**9+7
sums = [1]*(4*n)
muls = [1]*(4*n)

def mul(l, r, v, tl=0, tr=n-1, pos=1):
    if tl == l and tr == r:
        sums[pos] = (sums[pos]*v)%MOD
        muls[pos] = (muls[pos]*v)%MOD
    elif l <= r:
        tm = (tl+tr)//2
        mul(l, min(r, tm), v, tl, tm, 2*pos)
        mul(max(l, tm+1), r, v, tm+1, tr, 2*pos+1)
        sums[pos] = (muls[pos] * (sums[2*pos] + sums[2*pos+1])) % MOD

def query(l, r, tl=0, tr=n-1, pos=1):
    if l == tl and r == tr:
        return sums[pos]
    elif l > r:
        return 0
    tm = (tl+tr)//2
    return (muls[pos] * ((query(l, min(r, tm), tl, tm, 2*pos) + query(max(l, tm+1), r, tm+1, tr, 2*pos+1))) % MOD) %MOD

Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        mul(inp[1], inp[2]-1, inp[3])
    else:
        Q.append(query(inp[1], inp[2]-1))

print(*Q, sep="\n")
