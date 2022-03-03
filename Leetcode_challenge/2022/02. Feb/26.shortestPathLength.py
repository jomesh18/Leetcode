'''
847. Shortest Path Visiting All Nodes
Hard

2240

117

Add to List

Share
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:


Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
 

Constraints:

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.
Accepted
52,092
Submissions
85,570
'''
#dfs
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        def dp(node, mask):
            state = (node, mask)
            if state in cache: return cache[state]
            if mask & (mask-1) == 0: return 0
            cache[state] = float("inf")
            for neighbor in graph[node]:
                if mask & (1<<neighbor):
                    visited = 1+dp(neighbor, mask)
                    not_visited = 1+dp(neighbor, mask^(1<<node))
                    cache[state] = min(cache[state], visited, not_visited)
            return cache[state]
        
        cache = {}
        ending_mask = (1<<n)-1
        return min(dp(node, ending_mask) for node in range(n))

#bfs
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1: return 0
        ending_mask = (1<<n)-1
        steps = 0
        q = [(node, 1<<node) for node in range(n)]
        seen = set(q)
        
        while q:
            next_q = []
            for i in range(len(q)):
                node, mask = q[i]
                for neighbor in graph[node]:
                    new_mask = mask | (1<<neighbor)
                    if new_mask == ending_mask:
                        return steps+1
                    if (neighbor, new_mask) not in seen:
                        seen.add((neighbor, new_mask))
                        next_q.append((neighbor, new_mask))
            q = next_q
            steps += 1