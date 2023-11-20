
# segment tree for range updates and query

arr = [-1,2,4,1,7,1,3,2]


n = len(arr)
st = [0]*(4*n)
lazy = [0]*(4*n)


def add(start, end, value, tl=0, tr=n-1, pos=1):
    if lazy[pos] != 0:
        st[pos] += (tr-tl+1)*lazy[pos]
        if tl != tr:
            lazy[2*pos] += lazy[pos]
            lazy[2*pos+1] += lazy[pos]
        lazy[pos] = 0
    if start > end:
        return 0
        
    if start == tl and end == tr:
        st[pos] += (tr-tl+1)*value
        if start != end:
            lazy[2*pos] += value
            lazy[2*pos+1] += value
    elif start <= end:
        tm = (tl + tr)//2
        add(start, min(tm, end), value, tl, tm, 2*pos)
        add(max(start, tm+1), end, value, tm+1, tr, 2*pos+1)
        st[pos] = st[2*pos] + st[2*pos+1]

def query(start, end, tl=0, tr=n-1, pos=1):
    
    if lazy[pos] != 0:
        st[pos] += (tr-tl+1)*lazy[pos]
        if tl != tr:
            lazy[2*pos] += lazy[pos]
            lazy[2*pos+1] += lazy[pos]
        lazy[pos] = 0
    if start > end:
        return 0
    if start == tl and end == tr:
        return st[pos]
    elif start <= end:
        tm = (tl + tr)//2
        return query(start, min(tm, end), tl, tm, 2*pos) + query(max(start, tm+1), end, tm+1, tr, 2*pos+1)

def build(arr, tl=0, tr=n-1, pos=1):
    if tl == tr:
        st[pos] = arr[tl]
    else:
        tm = (tl+tr)//2
        build(arr, tl, tm, 2*pos)
        build(arr, tm+1, tr, 2*pos+1)
        st[pos] = st[2*pos] + st[2*pos+1]


build(arr)
print(st)
print(lazy)

add(0, 3, 3)
print(st)
print(lazy)
add(0, 3, 1)
print(st)
print(lazy)
add(0, 0, 2)
print(st)
print(lazy)
print(query(3,5))
print(st)
print(lazy)
# arr = [1,2,1]

