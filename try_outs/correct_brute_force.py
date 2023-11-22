with open('input.txt') as t:
    n, m = [int(i) for i in t.readline().split()]
    a = [int(i) for i in t.readline().split()]

    def find_max():
        curr_sum, max_sum = 0, 0
        for num in a:
            curr_sum = max(num, curr_sum+num)
            max_sum = max(max_sum, curr_sum)
        return str(max_sum)

    with open('correct.txt', 'w') as o:
        o.write(find_max()+"\n")
        for _ in range(m):
            j, b = [int(i) for i in t.readline().split()]
            a[j] = b
            o.write(find_max()+"\n")
