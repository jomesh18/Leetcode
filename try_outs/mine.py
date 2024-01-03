import sys 
# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('my_output.txt', 'w') 

with open('input.txt') as t:
    n, m = [int(i) for i in t.readline().split()]

    st = [[] for _ in range(4*n)]

    
    def query(l, r):
        return query_util(l, r, 0, n-1, 1)[0]

    def add(i, v, tl=0, tr=n-1, pos=1):
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

    with open('my_output.txt', 'w') as w:
        for _ in range(q):
            a, b, c = [int(i) for i in t.readline().split()]
            if a == 1:
                w.write(str(query(b-1, c-1))+"\n")
            else:
                update(b-1, c)
