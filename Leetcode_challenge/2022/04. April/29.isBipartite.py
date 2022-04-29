'''
785. Is Graph Bipartite?
Medium

4297

267

Add to List

Share
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
Accepted
289,875
Submissions
569,588
'''
#using bfs O(v+e)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        color_arr = [-1]*n
        
        def bipartite(i):
            color_arr[i] = 1
            q = [i]
            
            while q:
                l = len(q)
                temp = []
                for _ in range(l):
                    curr = q.pop()
                    for node in graph[curr]:
                        if color_arr[node] == color_arr[curr]: return False
                        elif color_arr[node] != -1: continue
                        color_arr[node] = 1-color_arr[curr]
                        temp.append(node)
                q = temp[:]
            return True
            
        for i in range(n):
            if color_arr[i] == -1:
                if not bipartite(i):
                    return False
                # print(color_arr)
        return True

#dfs    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n
        
        def dfs(i):
            for node in graph[i]:
                if color[node] != -1:
                    if color[node] == color[i]: return False
                else:
                    color[node] = 1-color[i]
                    if not dfs(node): return False
            return True
        
        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i): return False
        return True

#using union find
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        class UF:
            def __init__(self, n):
                self.root = [i for i in range(n)]
                self.rank = [0]*n
                
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px != py:
                    if self.rank[px] > self.rank[py]:
                        self.root[py] = px
                    elif self.rank[py] > self.rank[px]:
                        self.root[px] = py
                    else:
                        self.root[py] = px
                        self.rank[px] += 1

        uf = UF(n)

        for i in range(n):
            rooti = uf.find(i)
            for j in graph[i]:
                if uf.find(j) == rooti: return False
                uf.union(j, graph[i][0])
        return True