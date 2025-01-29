'''
684. Redundant Connection
Solved
Medium
Topics
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        cycle = []
        def dfs(node, cycle, parent):
            cycle.append(node)
            has_cycle = False
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in cycle:
                    cycle.append(nei)
                    return True
                has_cycle = has_cycle | dfs(nei, cycle, node)
                if has_cycle: return has_cycle
            cycle.pop()
            return has_cycle
            
        dfs(1, cycle, None)
        # print(cycle)
        last = cycle[-1]
        cyc = [cycle.pop()]
        while cycle and cycle[-1] != last:
            cyc.append(cycle.pop())
        # print(cyc)
        for i in range(n-1, -1, -1):
            if edges[i][0] in cyc and edges[i][1] in cyc:
                return edges[i]
        