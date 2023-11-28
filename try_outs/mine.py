# n, m = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]

with open('input.txt') as t:
    n = int(t.readline())
    a = [int(i) for i in t.readline().split()]
    m = int(t.readline())

    st = [0]*(4*n)

    def build(a, tl=0, tr=n-1, pos=1):
        if tl == tr:
            if tl & 1:
                st[pos] = -a[tl]
            else:
                st[pos] = a[tl]
        else:
            tm = (tl+tr)//2
            build(a, tl, tm, 2*pos)
            build(a, tm+1, tr, 2*pos+1)
            ans = 0
            if tl & 1:
                ans -= (st[2*pos]+st[2*pos+1])
            else:
                ans += (st[2*pos]+st[2*pos+1])
            # if (tm+1) & 1:
            #   ans -= st[2*pos+1]
            # else:
            #   ans += st[2*pos+1]
            st[pos] = ans

    build(a)

    def query(l, r, orig_l, tl=0, tr=n-1, pos=1,):
        if l==tl and r == tr:
            if orig_l & 1:
                return -st[pos]
            else:
                return st[pos]
        elif l > r:
            return 0
        tm = (tl+tr)//2
        return query(l, min(r, tm), orig_l, tl, tm, 2*pos) + query(max(r, tm+1), r, orig_l, tm+1, tr, 2*pos+1)

    def update(i, val, tl=0, tr=n-1, pos=1):
        if tl == tr:
            if i & 1:
                st[pos] = -val
            else:
                st[pos] = val
        else:
            tm = (tl+tr)//2
            if i <= tm:
                update(i, val, tl, tm, 2*pos)
            else:
                update(i, val, tm+1, tr, 2*pos+1)
            ans = 0
            if tl & 1:
                ans -= (st[2*pos]+st[2*pos+1])
            else:
                ans += (st[2*pos]+st[2*pos+1])
            # if (tm+1) & 1:
            #   ans -= st[2*pos+1]
            # else:
            #   ans += st[2*pos+1]
            st[pos] = ans

    with open('my_out.txt', 'w') as o:
        for _ in range(m):
            typ, b, c = [int(i) for i in t.readline().split()]
            if typ == 0:
                update(b-1, c)
            else:
                o.write(str(query(b-1, c-1, b-1))+"\n")
