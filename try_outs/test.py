import sys

# sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

max_ = [0]*(4*n)
add_down = [0]*(4*n)

def push(pos):
    max_[2*pos] += add_down[pos]
    max_[2*pos+1] += add_down[pos]
    add_down[2*pos] += add_down[pos]
    add_down[2*pos+1] += add_down[pos]
    add_down[pos] = 0

def add(l, r, v, tl=0, tr=n-1, pos=1):
    if l == tl and r == tr:
        max_[pos] += v
        add_down[pos] += v
    elif l <= r:
        if add_down[pos]:
            push(pos)
        tm = (tl+tr)//2
        add(l, min(tm, r), v, tl, tm, 2*pos)
        add(max(l, tm+1), r, v, tm+1, tr, 2*pos+1)
        max_[pos] = max(max_[2*pos], max_[2*pos+1])

def query(x, l, tl=0, tr=n-1, pos=1):
    if max_[pos] < x:
        return -1
    if tl == tr:
        return tl
    if add_down[pos]:
        push(pos)
    tm = (tl+tr)//2
    if tm >= l:
        i = query(x, l, tl, tm, 2*pos)
        if i != -1:
            return i
    return query(x, l, tm+1, tr, 2*pos+1)


Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        add(inp[1], inp[2]-1, inp[3])
        # print(inp)
        # print(max_[:10])
        # print(add_down[:10])
    else:
        Q.append(query(inp[1], inp[2]))

print(*Q, sep='\n')
