import sys

# sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

ops = [0]*(4*n)
vals = [0]*(4*n)

def add(l, r, v, tl=0, tr=n-1, pos=1):
    if tl == l and tr == r:
        ops[pos] += v
        vals[pos] += v
    elif l <= r:
        tm = (tl+tr)//2
        add(l, min(r, tm), v, tl, tm, 2*pos)
        add(max(l, tm+1), r, v, tm+1, tr, 2*pos+1)
        vals[pos] = ops[pos] * (r-l+1) + (vals[2*pos] + vals[2*pos+1])

def query(l, r, tl=0, tr=n-1, pos=1):
    if tl == l and tr == r:
        return vals[pos]
    elif l > r:
        return 0
    tm = (tl+tr)//2
    lef = query(l, min(r, tm), tl, tm, 2*pos)
    rig = query(max(l, tm+1), r, tm+1, tr, 2*pos+1)
    return ops[pos] * (r-l+1) + (lef + rig)

Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        add(inp[1], inp[2]-1, inp[3])
    else:
        Q.append(query(inp[1], inp[2]-1))

print(*Q, sep="\n")
