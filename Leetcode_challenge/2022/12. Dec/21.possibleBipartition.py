'''
886. Possible Bipartition
Medium

3205

71

Add to List

Share
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.
'''
# bfs
class Solution:
    def possibleBipartition(self, n: int, dislikes: [[int]]) -> bool:
        g = defaultdict(list)
        for v1, v2 in dislikes:
            g[v1].append(v2)
            g[v2].append(v1)
        def bfs(start):
            q = [start]
            set_[start] = 0
            while q:
                new_q = []
                for node in q:
                    curr_set = set_[node]
                    for neig in g[node]:
                        if set_[neig] == curr_set:
                            return False
                        if set_[neig] == -1:
                            set_[neig] = 1-curr_set
                            new_q.append(neig)
                q = new_q
            return True
        set_ = [-1]*(n+1) 
        for i in range(1, n+1):
            if set_[i] == -1:
                if not bfs(i): return False
        return True
    
# dfs
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        for v1, v2 in dislikes:
            g[v1].append(v2)
            g[v2].append(v1)
        def dfs(node):
            curr_set = set_[node]
            for nei in g[node]:
                if set_[nei] == curr_set:
                    return False
                if set_[nei] == -1:
                    set_[nei] = 1-curr_set
                    if not dfs(nei):
                        return False
            return True
        set_ = [-1]*(n+1) 
        for i in range(1, n+1):
            if set_[i] == -1:
                set_[i] = 0
                if not dfs(i):
                    return False
        return True

# union find
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        class UF:
            def __init__(self, n):
                self.root = [i for i in range(n)]
                self.rank = [1]*(n)
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py: return 
                if self.rank[px] > self.rank[py]:
                    self.root[py] = px
                elif self.rank[px] < self.rank[py]:
                    self.root[px] = py
                else:
                    self.root[py] = px
                    self.rank[px] += 1
        adj_list = [[] for _ in range(n+1)]
        for a, b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)
        uf = UF(n+1)
        for i in range(1, n+1):
            curr_set = uf.find(i)
            for nei in adj_list[i]:
                if uf.find(nei) == curr_set: return False
                uf.union(nei, adj_list[i][0])
        return True
            