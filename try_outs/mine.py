# import sys 
# # For getting input from input.txt file 
# sys.stdin = open('input.txt', 'r')  
  
# # Printing the Output to output.txt file 
# sys.stdout = open('my_output.txt', 'w') 

with open('input.txt') as t:
    n, q = [int(i) for i in t.readline().split()]

    st = [[] for _ in range(4*n)]

    def merge(a, b):
        num1, f1 = a
        num2, f2 = b
        ans = num1 + num2
        for i in range(len(f2)):
            if f2[i] > 0:
                for j in range(i+1, len(f1)):
                    if f1[j] > 0:
                        ans += f2[i]*f1[j]
        return [ans, [i+j for i, j in zip(f1, f2)]]

    def query_util(l, r, tl, tr, pos):
        if l > r:
            return [0, [0]*40]
        elif tl == l and tr == r:
            return st[pos]
        else:
            tm = (tl+tr)//2
            return merge(query_util(l, min(r, tm), tl, tm, 2*pos), query_util(max(l, tm+1), r, tm+1, tr, 2*pos+1))

    def query(l, r):
        return query_util(l, r, 0, n-1, 1)[0]

    def update(i, v, tl=0, tr=n-1, pos=1):
        if tl == tr:
            count = [0]*40
            count[v-1] = 1
            st[pos] = [0, count]
        else:
            tm = (tl+tr)//2
            if i <= tm:
                update(i, v, tl, tm, 2*pos)
            else:
                update(i, v, tm+1, tr, 2*pos+1)
            st[pos] = merge(st[2*pos], st[2*pos+1])

    def take_and_build():
        def build(a, tl=0, tr=n-1, pos=1):
            if tl == tr:
                count = [0]*40
                count[a[tl]-1] = 1
                st[pos] = [0, count]
            else:
                tm = (tl+tr)//2
                build(a, tl, tm, 2*pos)
                build(a, tm+1, tr, 2*pos+1)
                st[pos] = merge(st[2*pos], st[2*pos+1])

        arr = [int(i) for i in t.readline().split()]
        build(arr)

    take_and_build()

    with open('my_output.txt', 'w') as w:
        for _ in range(q):
            a, b, c = [int(i) for i in t.readline().split()]
            if a == 1:
                w.write(str(query(b-1, c-1))+"\n")
            else:
                update(b-1, c)
