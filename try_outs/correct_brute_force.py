# import sys 
# # For getting input from input.txt file 
# sys.stdin = open('input.txt', 'r')  
  
# # Printing the Output to output.txt file 
# sys.stdout = open('correct_output.txt', 'w')

with open('input.txt') as t:

    n, q = [int(i) for i in t.readline().split()]


    arr = [int(i) for i in t.readline().split()]

    with open('correct_output.txt', 'w') as w:
        for kk in range(q):
            a, b, c = [int(i) for i in t.readline().split()]
            if a == 1:
                ans = 0
                for i in range(b-1, c):
                    for j in range(b-1, i):
                        if arr[j] > arr[i]:
                            ans += 1
                print(ans)
                w.write(str(ans)+"\n")
            else:
                arr[b-1] = c
