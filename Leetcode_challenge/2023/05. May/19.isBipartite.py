'''
785. Is Graph Bipartite?
Medium

7090

332

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
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # bipartite graphs have even cycles, if it contains odd cycles it is not bipartite
        # that means bipartite graphs are two colorable
        # we are coloring the first vertex red (1) and the neighbors blue color (2)
        # we can use bfs for this
        
        n = len(graph)
        visited = [False]*n
        
        def bfs(i, visited):
            visited[i] = 1
            q = [i]
            color = 1
            nex_color = 2
            while q:
                nq = []
                for node in q:
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = nex_color
                            nq.append(nei)
                        else:
                            if visited[nei] != nex_color:
                                return False
                q = nq
                color, nex_color = nex_color, color
            return True
            
        for i in range(n):
            if not visited[i]:
                if not bfs(i, visited):
                    return False
        return True