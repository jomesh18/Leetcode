import sys 
# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('correct_output.txt', 'w')

with open('input.txt') as t:

    n, q = [int(i) for i in t.readline().split()]
    big_num = 10**9+1
    arr = [big_num]*n
    Q = []
    for kk in range(q):
        ins = [int(i) for i in t.readline().split()]
        a, b = ins[0], ins[1]
        if a == 1:
            arr[b] = ins[2]
        else:
            ans = 0
            for k in range(b, ins[2]):
                if arr[k] <= ins[3]:
                    ans += 1
                    arr[k] = 0
            Q.append(ans)

    print(*Q, sep="\n")