class SegmentTree:

    def __init__(self, n: int):
        self.segment = [0]*(4*n)
        self.lazy = [0]*(4*n)

    def update(self, start, end, delta, pos=0, lo=0, hi=None):
        if hi is None: hi = len(self.segment)-1
        if lo > hi:
            return 
        print(pos)
        if self.lazy[pos] != 0:
            self.segment[pos] += self.lazy[pos]
            if low !=  high:
                self.lazy[2*pos+1] += self.lazy[pos]
                self.lazy[2*pos+2] += self.lazy[pos]
            self.lazy[pos] = 0

        if lo >= start and hi <= end:
            self.segment[pos] += delta
            if lo != hi:
                self.lazy[2*pos+1] += delta
                self.lazy[2*pos+2] += delta
        else:
            mid = (lo+hi)//2
            self.update(start, end, delta, 2*pos+1, lo, mid)
            self.update(start, end, delta, 2*pos+2, mid+1, hi)
            self.segment[pos] = self.segment[2*pos+1]+self.segment[2*pos+2]

    def range_query(self, qlow, qhigh, pos=0, lo=0, hi=None):
        if hi is None: hi = len(self.segment)-1
        if lo > hi:
            return 0

        if self.lazy[pos] != 0:
            self.segment[pos] += self.lazy[pos]
            if lo != hi:
                self.lazy[2*pos+1] += self.lazy
                self.lazy[2*pos+2] += self.lazy
            self.lazy[pos] = 0

        if qlow > hi or qhigh < lo:
            return 0
        elif qlow <= lo and qhigh >= hi:
            return self.segment[pos]
        else:
            mid = (lo+hi)//2
            l = self.range_query(qlow, qhigh, 2*pos+1, lo, mid)
            r = self.range_query(qlow, qhigh, 2*pos+2, mid+1, hi)
            return l+r


nums = [2, 3, -1, 4]
segObj = SegmentTree(len(nums))

for i in range(len(nums)):
    segObj.update(i, i, nums[i])

print(segObj.segment)
print(segObj.lazy)

print(segObj.range_query(1, 2))
print(segObj.range_query(0, 3))
print(segObj.range_query(1, 3))
