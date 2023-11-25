# n, m = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]

with open('input.txt') as t:
    n, m = [int(i) for i in t.readline().split()]
    a = [0]*n

    st = [0]*(4*n)
    seen = [0]*(4*n)

    def push(i):
        if seen[i]:
            seen[2*i] = True
            seen[2*i+1] = True
            st[2*i] += val
            st[2*i+1] += val

    def query(i, tl=0, tr=n-1, pos=1):
        if tl == tr:
            return st[pos]
        tm = (tl+tr)//2
        if i <= tm:
            return query(i, tl, tm, 2*pos)
        else:
            return query(i, tm+1, tr, 2*pos+1)

    def update(l, r, val, tl=0, tr=n-1, pos=1):
        if l == tl and r == tr:
            st[pos] += val
            seen[pos] = True
        else:
            tm = (tl+tr)//2
            if i <= tm:
                update(i, val, tl, tm, 2*pos)
            else:
                update(i, val, tm+1, tr, 2*pos+1)

    with open('my_out.txt', 'w') as o:
        for _ in range(m):
            ins = [int(i) for i in t.readline().split()]
            if ins[0] == 1:
                # for k in range(ins[1], ins[2]):
                #     update(k, ins[3])
                update(ins[1], ins[2]-1, ins[3])
            else:
                o.write(str(query(ins[1]))+"\n")
