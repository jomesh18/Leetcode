with open('input.txt') as t:
    n = int(t.readline())
    a = [int(i) for i in t.readline().split()]
    m = int(t.readline())

    with open('correct.txt', 'w') as o:
        for _ in range(m):
            typ, b, c = [int(i) for i in t.readline().split()]
            if typ == 0:
                a[b-1] = int(c)
            else:
                ans = 0
                mul = 1
                for i in range(b-1, c):
                    ans += mul*a[i]
                    mul *= -1
                o.write(str(ans)+"\n")
