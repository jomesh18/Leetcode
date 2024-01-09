import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

lazy = [float('inf')]*(4*n)
vals = [0]*(4*n)

def push(pos, tl, tr):
    tm = (tl+tr)//2
    vals[2*pos] = lazy[pos] * (tm-tl+1)
    vals[2*pos+1] = lazy[pos] * (tr-tm+1+1)
    lazy[2*pos] = lazy[pos]
    lazy[2*pos+1] = lazy[pos]
    lazy[pos] = float('inf')

def assign(l, r, v, tl=0, tr=n-1, pos=1):
    if tl == l and tr == r:
        lazy[pos] = v
        vals[pos] = v * (tr-tl+1)
    elif l <= r:
        if lazy[pos] != float('inf'):
            push(pos, tl, tr)
        tm = (tl+tr)//2
        assign(l, min(r, tm), v, tl, tm, 2*pos)
        assign(max(l, tm+1), r, v, tm+1, tr, 2*pos+1)
        vals[pos] = vals[2*pos] + vals[2*pos+1]

def query(l, r, tl=0, tr=n-1, pos=1):
    if tl == l and tr == r:
        return vals[pos]
    elif l > r:
        return 0
    if lazy[pos] != float('inf'):
        return lazy[pos] * (r-l+1)
    tm = (tl+tr)//2
    lef = query(l, min(r, tm), tl, tm, 2*pos)
    rig = query(max(l, tm+1), r, tm+1, tr, 2*pos+1)
    return lef + rig

Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        assign(inp[1], inp[2]-1, inp[3])
        print(inp)
        print(vals[:12])
        print(lazy[:12])
    else:
        Q.append(query(inp[1], inp[2]-1))

print(*Q, sep="\n")
