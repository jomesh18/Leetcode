with open('input.txt') as t:
    r, n, m = [int(i) for i in t.readline().split()]

    def mul(a, b):
        a1, a2 = a[0]
        a3, a4 = a[1]
        b1, b2 = b[0]
        b3, b4 = b[1]
        ans = [[((a1*b1)%r+(a2*b3)%r)%r, ((a1*b2)%r+(a2*b4)%r)%r], [((a3*b1)%r+(a4*b3)%r)%r, ((a3*b2)%r+(a4*b4)%r)%r]]
        return ans

    a = []
    for _ in range(n):
        b = [[int(i) for i in t.readline().split()]]
        b.append([int(i) for i in t.readline().split()])
        a.append(b)
        t.readline()

    with open('correct.txt', 'w') as o:
        for k in range(m):
            b, c = [int(i) for i in t.readline().split()]
            ans = a[b-1]
            for i in range(b, c):
                ans = mul(ans, a[i])

            o.write(" ".join([str(i) for i in ans[0]])+"\n")
            o.write(" ".join([str(i) for i in ans[1]])+"\n")
            o.write("\n")


# if not filecmp.cmp('correct.txt', 'my_out.txt', shallow=False):
#     print("Not good")
# else:
#     print('Good')