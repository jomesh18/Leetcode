# n, m = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]

with open('input.txt') as t:
    r, n, m = [int(i) for i in t.readline().split()]
    st = [[] for _ in range(4*n)]

    def mul(a, b):
        a1, a2 = a[0]
        a3, a4 = a[1]
        b1, b2 = b[0]
        b3, b4 = b[1]
        ans = [[(a1*b1+a2*b3)%r, (a1*b2+a2*b4)%r], [(a3*b1+a4*b3)%r, (a3*b2+a4*b4)%r]]
        return ans

    def build(a, tl=0, tr=n-1, pos=1):
        if tl == tr:
            st[pos] = a[tl]
        else:
            tm = (tl+tr)//2
            build(a, tl, tm, 2*pos)
            build(a, tm+1, tr, 2*pos+1)
            st[pos] = mul(st[2*pos], st[2*pos+1])

    def query(l, r, tl=0, tr=n-1, pos=1,):
        if l==tl and r == tr:
            return st[pos]
        elif l > r:
            return [[1, 0], [0, 1]]
        tm = (tl+tr)//2
        return mul(query(l, min(r, tm), tl, tm, 2*pos), query(max(l, tm+1), r, tm+1, tr, 2*pos+1))

    a = []
    for _ in range(n):
        b = [[int(i) for i in t.readline().split()]]
        b.append([int(i) for i in t.readline().split()])
        a.append(b)
        t.readline()

    build(a)

    with open('my_out.txt', 'w') as o:
        for k in range(m):
            b, c = [int(i) for i in t.readline().split()]
            arr = query(b-1, c-1)
            o.write(" ".join(str(i) for i in arr[0])+"\n")
            o.write(" ".join(str(i) for i in arr[1])+"\n")
            o.write("\n")
