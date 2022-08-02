#segment tree for rangeMinQuery, by thushar roy
class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        next_power_of_2 = 
        self.tree = [0]*(2*next_power_of_2-1)
        self.construct_tree(arr, 0, len(self.tree), 0)

    def construct_tree(self, arr, lo, hi, pos):
        if lo == hi:
            self.tree[pos] = arr[lo]
            return
        mid = (lo+hi)//2
        self.construct_tree(arr, lo, mid, 2*pos+1)
        self.construct_tree(arr, mid+1, hi, 2*pos+2)
        self.tree[pos] = min(self.tree[2*pos+1], self.tree[2*pos+2])

    def query_tree(self, arr, qleft, qright, left=0, right=len(self.tree)-1, pos=0):
        if qleft <= left and right <= qright:
            return self.tree[pos]
        elif qleft > left or right > qright:
            return float('inf')
        mid = (left+right)//2
        return min(self.query_tree, arr, )


    def update_tree(self, index, value):
