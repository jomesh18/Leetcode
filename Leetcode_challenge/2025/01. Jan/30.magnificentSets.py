'''
2493. Divide Nodes Into the Maximum Number of Groups
Solved
Hard
Topics
Companies
Hint
You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

 

Example 1:


Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.
Example 2:

Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.
 

Constraints:

1 <= n <= 500
1 <= edges.length <= 104
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There is at most one edge between any pair of vertices.
'''
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a-1].append(b-1)
            adj_list[b-1].append(a-1)
        
        colors = [-1]*n
        for i in range(n):
            if colors[i] == -1:
                colors[i] = 0
                if not self._check_if_bipartite(i, adj_list, colors):
                    return -1

        distances = [0]*n
        for i in range(n):
            distances[i] = self._find_shortest_distance(i, adj_list, n)
        
        max_number_of_groups = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                max_number_of_groups += self._find_group_size(i, adj_list, distances, visited)
        return max_number_of_groups

    def _check_if_bipartite(self, node, adj_list, colors):
        for nei in adj_list[node]:
            if colors[nei] == colors[node]:
                return False
            if colors[nei] != -1:
                continue
            colors[nei] = 1-colors[node]
            if not self._check_if_bipartite(nei, adj_list, colors):
                return False
        return True
    
    def _find_shortest_distance(self, node, adj_list, n):
        d = 0
        q = deque([node])
        visited = [False]*n
        visited[node] = True
        while q:
            l = len(q)
            for _ in range(l):
                curr = q.popleft()
                for nei in adj_list[curr]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
            d += 1
        return d

    def _find_group_size(self, node, adj_list, distances, visited):
        max_g = distances[node]
        for nei in adj_list[node]:
            if visited[nei]: continue
            visited[nei] = True
            max_g = max(max_g, self._find_group_size(nei, adj_list, distances, visited))
        return max_g
    