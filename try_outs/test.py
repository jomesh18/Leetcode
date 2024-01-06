import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

ors = [0]*(4*n)
ands = [1]*(4*n)

def build(i, tl=0, tr=n-1, pos=1):
    if tl == tr:
        ands[pos] = 0
    else:
        tm = (tl+tr)//2
        if i <= tm:
            build(i, tl, tm, 2*pos)
        else:
            build(i, tm+1, tr, 2*pos+1)

for i in range(n):
    build(i)

def apply_or(l, r, v, tl=0, tr=n-1, pos=1):
    if tl == l and tr == r:
        ors[pos] |= v
        ands[pos] |= v
    elif l <= r:
        tm = (tl+tr)//2
        apply_or(l, min(r, tm), v, tl, tm, 2*pos)
        apply_or(max(l, tm+1), r, v, tm+1, tr, 2*pos+1)
        ands[pos] = ors[pos] & (ands[2*pos] | ands[2*pos+1])

def find_and(l, r, tl=0, tr=n-1, pos=1):
    if tl == l and tr == r:
        return ands[pos]
    elif l > r:
        return 0
    tm = (tl+tr)//2
    return ands[pos] & (find_and(l, min(r, tm), tl, tm, 2*pos) | find_and(max(l, tm+1), r, tm+1, tr, 2*pos+1))

Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        apply_or(inp[1], inp[2]-1, inp[3])
    else:
        Q.append(find_and(inp[1], inp[2]-1))
    print(inp)
    print(ors[:10])
    print(ands[:10])

print(*Q, sep="\n")
