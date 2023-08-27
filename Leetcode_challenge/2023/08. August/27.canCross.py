class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {val : i for i, val in enumerate(stones)}
        memo = {}
        visited = set()
        def helper(i, k):
            # print(i, k)
            if i >= len(stones)-1:
                return True
            if (i, k) in memo: return memo[(i, k)]
            ans = False
            if stones[i] + k in d and (d[stones[i]+k], k) not in visited:
                visited.add((d[stones[i]+k], k))
                if helper(d[stones[i]+k], k):
                    ans = True
            if stones[i] + k+1 in d and (d[stones[i]+k+1], k+1) not in visited:
                visited.add((d[stones[i]+k+1], k+1))
                if helper(d[stones[i]+k+1], k+1):
                    ans = True
            if stones[i] + (k-1) in d and (d[stones[i]+k-1], k-1) not in visited:
                visited.add((d[stones[i]+k-1], k-1))
                if helper(d[stones[i]+k-1], k-1):
                    ans = True
            memo[(i, k)] = ans
            return ans
        return helper(d[stones[0]+1], 1) if stones[0] + 1 in d else False