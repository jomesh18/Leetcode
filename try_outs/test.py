import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

res = [0]*(4*n)
add_down = [0]*(4*n)
replace_down = [0]*(4*n)

def push_replace(pos, tl, tr):
    tm = (tl+tr)//2
    left = (tm-tl+1)
    right = (tr-tm)
    res[2*pos] = replace_down[pos] * left
    res[2*pos+1] = replace_down[pos] * right
    replace_down[2*pos] = replace_down[pos]
    replace_down[2*pos+1] = replace_down[pos]
    add_down[pos] = 0
    replace_down[pos] = 0

def push_add_down(pos, tl, tr):
    if replace_down[pos]:
        replace_down[pos] += add_down[pos]
        push_replace(pos, tl, tr)
    else:
        tm = (tl+tr)//2
        left = (tm-tl+1)
        right = (tr-tm)
        res[2*pos] += add_down[pos] * left
        res[2*pos+1] += add_down[pos] * right
        if replace_down[2*pos]:
            replace_down[2*pos] += add_down[pos]
            add_down[2*pos] = 0
        else:
            add_down[2*pos] += add_down[pos]
        if replace_down[2*pos+1]:
            replace_down[2*pos+1] += add_down[pos]
            add_down[2*pos+1] = 0
        else:
            add_down[2*pos+1] += add_down[pos]
        add_down[pos] = 0


def replace(l, r, v, tl=0, tr=n-1, pos=1):
    if l == tl and r == tr:
        res[pos] = v * (tr-tl+1)
        replace_down[pos] = v
        add_down[pos] = 0
    elif l <= r:
        replace_down[pos] = 0
        add_down[pos] = 0
        tm = (tl+tr)//2
        replace(l, min(r, tm), v, tl, tm, 2*pos)
        replace(max(l, tm+1), r, v, tm+1, tr, 2*pos+1)
        res[pos] = res[2*pos] + res[2*pos+1]

def add(l, r, v, tl=0, tr=n-1, pos=1):
    if l == tl and r == tr:
        res[pos] += v * (tr-tl+1)
        add_down[pos] += v 
        if tl != tr:
            if replace_down[pos]:
                replace_down[pos] += v
                push_replace(pos, tl, tr)
    elif l <= r:
        if add_down[pos]:
            push_add_down(pos)
        tm = (tl+tr)//2
        add(l, min(tm, r), v, tl, tm, 2*pos)
        add(max(l, tm+1), r, v, tm+1, tr, 2*pos+1)
        res[pos] = res[2*pos] + res[2*pos+1]

def query(l, r, tl=0, tr=n-1, pos=1):
    if l == tl and r == tr:
        return res[pos]
    elif l > r:
        return 0
    if replace_down[pos]:
        push_replace(pos, tl, tr)
    if add_down[pos]:
        push_add_down(pos, tl, tr)
    tm = (tl+tr)//2
    left = query(l, min(tm, r), tl, tm, 2*pos)
    right = query(max(l, tm+1), r, tm+1, tr, 2*pos+1)
    return left + right

Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        replace(inp[1], inp[2]-1, inp[3])
        # print(inp)
        # print(max_[:10])
        # print(add_down[:10])
    elif inp[0] == 2:
        add(inp[1], inp[2]-1, inp[3])
    else:
        Q.append(query(inp[1], inp[2]-1))

print(*Q, sep='\n')
