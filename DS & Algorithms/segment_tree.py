#segment tree for rangeMinQuery, by thushar roy
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        k = 1
        while k < self.n:
            k <<= 1
        self.tree = [float('inf')]*k
        self.lazy = [0]*k
        self.create(arr, 0, self.n-1, 0)

    def create(self, arr, lo, hi, pos):
        if lo == hi:
            self.tree[pos] = arr[lo]
        else:
            mid = (lo+hi)//2
            self.create(arr, lo, mid, pos*2+1)
            self.create(arr, mid+1, hi, pos*2+2)
            self.tree[pos] = min(self.tree[2*pos+1], self.tree[2*pos+2])


    def update_index(self, index, value):
        self.update_tree(index, index, value)

    def update_range(self, start, end, delta):
        self.update_tree(start, end, delta)

    def update_tree(self, start, end, delta, lo=0, hi=self.n-1, pos=0):

        if lo > hi: return
        if self.lazy[pos] != 0:
            self.tree[pos] += self.lazy[pos]
            if lo != hi:
                self.lazy[pos*2+1] += self.lazy[pos]
                self.lazy[pos*2+2] += self.lazy[pos]
            
            self.lazy[pos] = 0
        if start > hi or end < lo:
            return
        if start <= lo and end >= hi:
            self.tree[pos] += delta
            if lo != hi:
                lazy[2*pos+1] += delta
                lazy[2*pos+2] += delta
            return
        mid = (lo+hi)//2
        self.update_tree(start, end, delta, lo, mid, 2*pos+1)
        self.update_tree(start, end, delta, mid+1, hi, 2*pos+2)
        self.tree[pos] = min(self.tree[2*pos+1], self.tree[2*pos+1])

    def range_min_query_lazy(self, qleft, qright, left=0, right=len(self.tree)-1, pos=0):
        if left > right:
            return float('inf')      
        if self.lazy[pos] != 0:
            self.tree[pos] += self.lazy[pos]
            if left != right:
                self.lazy[2*pos+1] = self.lazy[pos]
                self.lazy[2*pos+2] = self.lazy[pos]
            self.lazy[pos] = 0

        if qleft <= left and qright >= right:
            return self.tree[pos]
        elif qleft > left or qright < right:
            return float('inf')
        mid = (left+right)//2
        return min(self.range_min_query_lazy(qleft, qright, left, mid, 2*pos+1), self.range_min_query_lazy(arr, qleft, qright, mid+1, right, 2*pos+2))
