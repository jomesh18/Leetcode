# class Solution:
#     def sumCounts(self, nums: List[int]) -> int:
#         n = len(nums)
#         sum_sq = 0
#         res = 0
#         count = [0]*(n+1)
#         last = [0]*(n+1)
#         for i in range(n):
#             l = last[nums[i]]
#             curr_sum = sum(count[l:i])
#             for k in range(l, i+1):
#                 count[k] += 1
#             sum_sq += 2*curr_sum+(i-l)+1
#             res += sum_sq
#             last[nums[i]] = i+1
#         return res
        
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        sum_sq = 0
        res = 0
        last = {}
        st = [0]*4*n
        lazy = [0]*4*n

        def query(l, r, v=1, tl=0, tr=n-1):
            if l > r:
                return 0
            elif tl == l and tr == r:
                return (lazy[v]*(tr-tl) + st[v])%MOD
            tm = (tl + tr)//2
            return (
                (r-l)*lazy[v] + 
                query(l, min(r, tm), 2*v, tl, tm) + 
                query(max(l, tm+1), r, 2*v+1, tm+1, tr)
                ) % MOD

        def update(l, r, add, v=1, tl=0, tr=n-1):
            if l == tl and r == tr:
                lazy[v] += add
            elif l <= r:
                lazy[2*v] += lazy[v]
                lazy[2*v+1] += lazy[v]
                lazy[v] = 0
                tm = (tl+tr)//2
                update(l, min(r, tm), add, 2*v, tl, tm)
                update(max(tm+1, l), r, add, 2*v+1, tm+1, tr)
                st[v] = query(tl, tm, 2*v, tl, tm) + query(tm+1, tr, v*2+1, tm+1, tr)

        for i in range(n):
            l = last.get(nums[i], 0)
            curr_sum = query(l, i)
            update(l, i, 1)
            sum_sq = (sum_sq+2*curr_sum+(i-l)+1)%MOD
            res = (res+sum_sq)%MOD
            last[nums[i]] = i+1
            print(st)
        return res