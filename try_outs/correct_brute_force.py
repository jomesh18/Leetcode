with open('input.txt') as t:
    n, m = [int(i) for i in t.readline().split()]
    a = [0]*n

    with open('correct.txt', 'w') as o:
        for _ in range(m):
            ins = [int(i) for i in t.readline().split()]
            if ins[0] == 1:
                for i in range(ins[1], ins[2]):
                    a[i] += ins[3]
            else:
                o.write(str(a[ins[1]])+"\n")
