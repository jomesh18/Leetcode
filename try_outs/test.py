import sys

n, m = map(int, sys.stdin.readline().split())
st = [0]*(4*n)
big_num = 
    
def query(l, r, v, tl=0, tr=n-1, pos=1):
    if tl == tr:
        return st[pos]
    elif l > r:
        return big_num
    tm = (tl+tr)//2
    lef = query(l, min(r, tm), tl, tm, 2*pos)
    rig = query(max(l, tm+1), r, tm+1, tr, 2*pos+1)
    return lef + rig

def update(i, v, tl=0, tr=n-1, pos=1):
    if tl == tr:
        st[pos] = [[v, 1]]
    else:
        tm = (tl+tr)//2
        if i <= tm:
            update(i, v, tl, tm, 2*pos)
        else:
            update(i, v, tm+1, tr, 2*pos+1)
        print(st)
        st[pos] = merge(st[2*pos], st[2*pos+1])

Q = []
for _ in range(m):
    ins = list(map(int, sys.stdin.readline().split()))
    if ins[0] == 1:
        update(ins[1], ins[2])
    else:
        Q.append(query(ins[1], ins[2]-1, ins[3]))

print(*Q, sep="\n")
