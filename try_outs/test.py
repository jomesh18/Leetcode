import sys 
# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('my_output.txt', 'w')

# n, m = map(int, sys.stdin.readline().split())
n, m = map(int, input().split())
# big_num = 10**9+1
big_num = 10
st = [(big_num, n)]*(4*n)
print(st)
def merge(a, b):
    if a[0] <= b[0]:
        return a
    else:
        return b
    
def query(l, r, tl=0, tr=n-1, pos=1):
    if tl == tr:
        return st[pos]
    elif l > r:
        return (big_num, n)
    tm = (tl+tr)//2
    lef = query(l, min(r, tm), tl, tm, 2*pos)
    rig = query(max(l, tm+1), r, tm+1, tr, 2*pos+1)
    return merge(lef, rig)

def update(i, v, tl=0, tr=n-1, pos=1):
    if tl == tr:
        st[pos] = (v, i)
    else:
        tm = (tl+tr)//2
        if i <= tm:
            update(i, v, tl, tm, 2*pos)
        else:
            update(i, v, tm+1, tr, 2*pos+1)
        st[pos] = merge(st[2*pos], st[2*pos+1])

Q = []
for _ in range(m):
    ins = list(map(int, sys.stdin.readline().split()))
    if ins[0] == 1:
        update(ins[1], ins[2])
        print(st)
    else:
        ans = 0
        l, r, p = ins[1], ins[2]-1, ins[3]
        while True:
            min_, i = query(l, r)
            print(min_, i, l, r)
            if min_ > p:
                Q.append(ans)
                break
            else:
                ans += 1
                update(i, big_num)
                print('st', st[15], st[7], st[3], st[1], st)

print(*Q, sep="\n")
