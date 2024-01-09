import sys

# # For getting input from input.txt file 
# sys.stdin = open('input.txt', 'r')

MOD = 10**9+7

n, m = [int(i) for i in sys.stdin.readline().split()]
arr = [0]*n
Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        for i in range(inp[1], inp[2]):
            arr[i] = inp[3]
    else:
        Q.append(sum(arr[inp[1]: inp[2]]))

print(*Q, sep="\n")
