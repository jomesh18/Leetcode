import sys

# # For getting input from input.txt file 
# sys.stdin = open('input.txt', 'r')

# MOD = 10**9+7

n, m = [int(i) for i in sys.stdin.readline().split()]
arr = [0]*n
Q = []
for _ in range(m):
    inp = list(map(int, sys.stdin.readline().split()))
    # if inp[0] == 1:
    for i in range(inp[0], inp[1]):
        arr[i] = inp[2]
    # else:
    max_sum = 0
    curr_sum = 0
    for num in arr:
        curr_sum = max(curr_sum+num, 0)
        max_sum = max(max_sum, curr_sum)
    Q.append(max_sum)

print(*Q, sep="\n")
