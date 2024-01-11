import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

s = [0]*(4*n)
change = [0]*(4*n)

def push(pos, tl, tr):
    tm = (tl+tr)//2
    s[2*pos] = (tm-tl+1)-s[2*pos]
    s[2*pos+1] = (tr-tm)-s[2*pos+1]
    change[2*pos] = 1 - change[2*pos]
    change[2*pos+1] = 1 - change[2*pos+1]

def complement(l, r, tl=0, tr=n-1, pos=1):
    if l == tl and r == tr:
        change[pos] = 1 - change[pos]
        s[pos] = (r-l+1)-s[pos]
        print(r, l, pos, s[pos])
        return
    elif l <= r:
        tm = (tl+tr)//2
        if change[pos]:
            push(pos, tl, tr)
        complement(l, min(r, tm), tl, tm, 2*pos)
        complement(max(l, tm+1), r, tm+1, tr, 2*pos+1)
        s[pos] = s[2*pos] + s[2*pos+1]

def query(k, tl=0, tr=n-1, pos=1):
    if tl == tr:
        return tl
    else:
        tm = (tl+tr)//2
        if s[pos] >= k:
            return query(k, tl, tm, 2*pos)
        else:
            return query(k-s[pos], tm+1, tr, 2*pos+1)

Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        complement(inp[1], inp[2]-1)
        print(inp)
        print(s[:10])
        print(change[:10])
    else:
        Q.append(query(inp[1]))

print(*Q, sep="\n")
