n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

class Node:
    def __init__(self, max_sum, pref, suff, sum):
        self.max_sum = max_sum
        self.pref = pref
        self.suff = suff
        self.sum = sum

st = [0]*(4*n)

def combine(a, b):
    curr = Node(0, 0, 0, 0)
    curr.max_sum = max(0, a.max_sum, b.max_sum, a.suff+b.pref)
    curr.sum = a.sum+b.sum
    curr.pref = max(a.pref, a.sum+b.pref)
    curr.suff = max(b.suff, b.sum+a.suff)
    return curr

def build(a, tl=0, tr=n-1, pos=1):
    if tl == tr:
        st[pos] = Node(a[tl], a[tl], a[tl], a[tl])
    else:
        tm = (tl+tr)//2
        build(a, tl, tm, 2*pos)
        build(a, tm+1, tr, 2*pos+1)
        st[pos] = combine(st[2*pos], st[2*pos+1])

def set(i, val, tl=0, tr=n-1, pos=1):
    if tl == tr:
        st[pos] = Node(val, val, val, val)
    else:
        tm = (tl+tr)//2
        if i <= tm:
            set(i, val, tl, tm, 2*pos)
        else:
            set(i, val, tm+1, tr, 2*pos+1)
        st[pos] = combine(st[2*pos], st[2*pos+1])

def find_max(tl=0, tr=n-1, pos=1):
    return st[1].max_sum

build(a)
print(find_max())
for _ in range(m):
    a, b = [int(i) for i in input().split()]
    set(a, b)
    print(find_max())


# 4 2
# -2 -1 -5 -4
# 1 3
# 3 2