# Binary indexed tree/ Fenwick tree
# for prefix sum with update

class BIT:
    def __init__(self, n):
        self.bit = [0]*(n+1)

    def sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i = self.get_parent(i)
        return s

    def update(self, i, delta):
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i = self.get_next(i)

    def get_next(self, i):
        return i + (i & -i)

    def get_parent(self, i):
        return i - (i & -i)

arr = [1, 2, 3, 4]
bit = BIT(len(arr))
print(bit.bit)
for i in range(len(arr)):
    bit.update(i, arr[i])
print(bit.bit)
print(bit.sum(2))
#update index 2 value to 0
old_val = arr[2]
new_val = 0
bit.update(2, -old_val+new_val)
print(bit.sum(2))
