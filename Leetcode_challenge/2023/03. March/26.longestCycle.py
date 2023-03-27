'''
2360. Longest Cycle in a Graph
Hard

1872

36

Add to List

Share
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

 

Example 1:


Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
Example 2:


Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.
 

Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
'''
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        def dfs(node, dist):
            # print(node, dist)
            visited[node] = True
            nei = edges[node]
            if nei != -1 and (not visited[nei]):
                dist[nei] = dist[node] + 1
                dfs(nei, dist)
            elif nei != -1 and nei in dist:
                self.ans = max(self.ans, dist[node]-dist[nei]+1)
        
        self.ans = -1
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                dfs(i, {i: 1})
        return self.ans

# Kahns algo, topological sorting
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0]*n
        for e in edges:
            if e != -1:
                indegree[e] += 1
        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        visited = [False]*n
        while q:
            curr = q.pop()
            visited[curr] = True
            nei = edges[curr]
            if nei != -1:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        ans = -1
        for i in range(n):
            if not visited[i]:
                nei = edges[i]
                c = 1
                visited[i] = True
                while nei != i:
                    c += 1
                    visited[nei] = True
                    nei = edges[nei]
                ans = max(ans, c)
        return ans
                    