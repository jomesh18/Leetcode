import sys 

# # For getting input from input.txt file 
# sys.stdin = open('input.txt', 'r')
  
# # Printing the Output to output.txt file 
# sys.stdout = open('my_output.txt', 'w')

n, m = map(int, sys.stdin.readline().split())

st = [(0, 0)]*(4*n)

def add(l, r, v, tl=0, tr=n-1, pos=1):
    if l == tl and r == tr:
        st[pos] = (st[pos][0]+v, st[pos][1]+v)
    elif l <= r:
        tm = (tl+tr)//2
        add(l, min(r, tm), v, tl, tm, 2*pos)
        add(max(l, tm+1), r, v, tm+1, tr, 2*pos+1)
        st[pos] = (min(st[2*pos][0], st[2*pos+1][0])+st[pos][1], st[pos][1])

def query(l, r, tl=0, tr=n-1, pos=1):
    if l == tl and r == tr:
        return st[pos][0]
    if l > r:
        return float('inf')
    tm = (tl+tr)//2
    
    return st[pos][1] + min(query(l, min(r, tm), tl, tm, 2*pos), query(max(l, tm+1), r, tm+1, tr, 2*pos+1))

Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        add(inp[1], inp[2]-1, inp[3])
    else:
        Q.append(query(inp[1], inp[2]-1))

print(*Q, sep="\n")
