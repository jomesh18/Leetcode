class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = [(headID, 0)]
        t = 0
        sub = [[] for _ in range(n)]
        for i, v in enumerate(manager):
            if v != -1:
                sub[v].append(i)
        # print(sub)
        while q:
            nq = []
            for man, curr_time in q:
                t = max(t, curr_time)
                for subordinate in sub[man]:
                    nq.append((subordinate, curr_time+informTime[man]))
                    
            q = nq
            # print(q)
        return t