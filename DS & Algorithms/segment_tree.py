#segment tree for rangeMinQuery, by thushar roy
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        k = 1
        while k < self.n:
            k <<= 1
        self.tree = [float('inf')]*(2*k-1)
        self.lazy = [0]*(2*k-1)
        self.create(arr, 0, self.n-1, 0)

    def create(self, arr, lo, hi, pos):
        if lo == hi:
            # print(lo, hi, self.tree, arr)
            self.tree[pos] = arr[lo]
        else:
            mid = (lo+hi)//2
            self.create(arr, lo, mid, pos*2+1)
            self.create(arr, mid+1, hi, pos*2+2)
            self.tree[pos] = min(self.tree[2*pos+1], self.tree[2*pos+2])

    def update_tree(self, start, end, delta, lo, hi, pos):

        if lo > hi: return
        if self.lazy[pos] != 0:
            self.tree[pos] += self.lazy[pos]
            if lo != hi:
                self.lazy[2*pos+1] += self.lazy[pos]
                self.lazy[2*pos+2] += self.lazy[pos]
            
            self.lazy[pos] = 0
        if start > hi or end < lo:
            return
        if start <= lo and end >= hi:
            self.tree[pos] += delta
            if lo != hi:
                self.lazy[2*pos+1] += delta
                self.lazy[2*pos+2] += delta
            return
        mid = (lo+hi)//2
        self.update_tree(start, end, delta, lo, mid, 2*pos+1)
        self.update_tree(start, end, delta, mid+1, hi, 2*pos+2)
        self.tree[pos] = min(self.tree[2*pos+1], self.tree[2*pos+2])

    def range_min_query(self, qleft, qright):
        return self.range_min_query_lazy(qleft, qright, 0, self.n-1, 0)

    def range_min_query_lazy(self, qleft, qright, left, right, pos):
        if left > right:
            return float('inf')      
        if self.lazy[pos] != 0:
            self.tree[pos] += self.lazy[pos]
            if left != right:
                self.lazy[2*pos+1] += self.lazy[pos]
                self.lazy[2*pos+2] += self.lazy[pos]
            self.lazy[pos] = 0

        if qleft <= left and qright >= right:
            return self.tree[pos]
        elif qleft > right or qright < left:
            return float('inf')
        mid = (left+right)//2
        return min(self.range_min_query_lazy(qleft, qright, left, mid, 2*pos+1), self.range_min_query_lazy(qleft, qright, mid+1, right, 2*pos+2))

    def update_index(self, index, value):
        self.update_tree(index, index, value, 0, self.n-1, 0)

    def update_range(self, start, end, delta):
        self.update_tree(start, end, delta, 0, self.n-1, 0)


arr = [-1,2,4,1,7,1,3,2]

tree = SegmentTree(arr)
print(tree.tree)
tree.update_range(0, 3, 3)
print(tree.tree)
tree.update_range(0, 3, 1)
print(tree.tree)
tree.update_index(0, 2)
print(tree.tree)
print(tree.range_min_query(3, 5))
print(tree.tree)