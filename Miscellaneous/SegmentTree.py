class SegmentTree:

    def __init__(self, nums: int):
        self.n = len(nums)
        curr = 1
        while curr < self.n:
            curr <<= 1
        seg_size = curr*2-1

        self.segment = [0]*seg_size
        self.lazy = [0]*seg_size
        self.build(0, self.n-1, 0, nums)

    def build(self, lo, hi, pos, nums):
        if(lo == hi):
            self.segment[pos] = nums[lo]
        else:
            mid = (lo + hi)//2;
            self.build(lo, mid, 2 * pos + 1, nums);
            self.build(mid + 1, hi, 2 * pos + 2, nums);
            self.segment[pos] = self.segment[2*pos+1]+self.segment[2*pos+2]

    def update(self, start, end, delta, pos, lo, hi):
        if lo > hi:
            return 
        if self.lazy[pos] != 0:
            self.segment[pos] += self.lazy[pos]
            if low != high:
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

    def range_query_util(self, qlow, qhigh):
        return self.range_query(qlow, qhigh, 0, 0, self.n-1)

    def range_query(self, qlow, qhigh, pos, lo, hi):
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
segObj = SegmentTree(nums)

print(segObj.segment)
print(segObj.lazy)

print(segObj.range_query_util(1, 2))
print(segObj.range_query_util(0, 3))
print(segObj.range_query_util(1, 3))
