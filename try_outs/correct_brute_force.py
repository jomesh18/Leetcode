n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    if a == 1:
        a[b] = c
    else:
        print(sum(a[b:c]))
