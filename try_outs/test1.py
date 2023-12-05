
import os, io, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def get_int():
    return map(int, input().split())

def get_list():
    return list(map(int, input().split()))

class Node:
    def __init__(self):
        self.count = 0
        self.f = [0]*40

    def merge(self, left, right):
        count = left.count + right.count
        for i in range(39, -1, -1):
            if left.f[i] > 0:
                for j in range(i):
                    if right.f[j] > 0:
                        count += left.f[i]*right.f[j]
            self.f[i] = left.f[i] + right.f[i]
        self.count = count

    def __str__(self):
        return str(self.count) +" "+ str([self.f[i] for i in range(40)])

n, q = get_list()

st = [0]*(4*n)

def query_util(l, r, tl, tr, pos):
    if l > r:
        return Node()
    elif tl == l and tr == r:
        return st[pos]
    tm = (tl+tr)//2
    res = Node()
    res.merge(query_util(l, min(r, tm), tl, tm, 2*pos), query_util(max(l, tm+1), r, tm+1, tr, 2*pos+1))
    return res

def query(l, r):
    return query_util(l, r, 0, n-1, 1).count

def update(i, v, tl=0, tr=n-1, pos=1):
    if tl == tr:
        st[pos] = Node()
        st[pos].f[v-1] = 1
    else:
        tm = (tl+tr)//2
        if i <= tm:
            update(i, v, tl, tm, 2*pos)
        else:
            update(i, v, tm+1, tr, 2*pos+1)
        st[pos] = Node()
        st[pos].merge(st[2*pos], st[2*pos+1])

def take_and_build():
    def build(a, tl=0, tr=n-1, pos=1):
        if tl == tr:
            st[pos] = Node()
            st[pos].count = 0
            st[pos].f[a[tl]-1] = 1
        else:
            tm = (tl+tr)//2
            build(a, tl, tm, 2*pos)
            build(a, tm+1, tr, 2*pos+1)
            st[pos] = Node()
            st[pos].merge(st[2*pos], st[2*pos+1])

    arr = get_list()
    build(arr)

take_and_build()

for _ in range(q):
    a, b, c = get_list()
    if a == 1:
        sys.stdout.write(str(query(b-1, c-1))+"\n")
    else:
        update(b-1, c)
 