# n, m = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]

with open('input.txt') as t:
    n, m = [int(i) for i in t.readline().split()]
    a = [int(i) for i in t.readline().split()]

    class Node:
        def __init__(self, max_sum, pref, suff, sum):
            self.max_sum = max(0, max_sum)
            self.pref = pref
            self.suff = suff
            self.sum = sum

        # def __str__(self):
        #     return f"{self.max_sum} {self.pref} {self.suff} {self.sum}"

    st = [0]*(4*n)

    def combine(a, b):  
        curr = Node(0, 0, 0, 0)
        curr.max_sum = max(a.max_sum, b.max_sum, a.suff+b.pref)
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
        # print(st[1])
        return str(st[1].max_sum)

    build(a)
    with open('my_out.txt', 'w') as o:
        o.write(find_max()+"\n")
        for _ in range(m):
            # a, b = [int(i) for i in input().split()]
            ind, val = [int(i) for i in t.readline().split()]
            # print(ind, val)
            set(ind, val)
            o.write(find_max()+"\n")
