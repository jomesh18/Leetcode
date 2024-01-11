import sys

# # For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')

# MOD = 10**9+7

n, m = [int(i) for i in sys.stdin.readline().split()]
arr = [0]*n
Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        for i in range(inp[1], inp[2]):
            arr[i] = 1-arr[i]
    else:
        k = inp[1]
        for i, num in enumerate(arr):
            if num == 1:
                if k == 0:
                    Q.append(i)
                    break
                else:
                    k -= 1

print(*Q, sep="\n")
