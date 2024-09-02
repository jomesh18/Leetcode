'''
2699. Modify Graph Edge Weights
Hard

670

145

Add to List

Share
You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.

Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.

Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.

Note: You are not allowed to modify the weights of edges with initial positive weights.

 

Example 1:



Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.
Example 2:



Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
Output: []
Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.
Example 3:



Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.
 

Constraints:

1 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= ai, bi < n
wi = -1 or 1 <= wi <= 107
ai != bi
0 <= source, destination < n
source != destination
1 <= target <= 109
The graph is connected, and there are no self-loops or repeated edges
'''
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        INF = target + 1
        def dijkstra(start, end, adj):
            min_distances = [INF]*n
            min_distances[start] = 0
            heap = [(0, start)]
            while heap:
                curr_d, curr_node = heappop(heap)
                if curr_d > min_distances[curr_node]:
                    continue
                for nei, w in adj[curr_node]:
                    if w + curr_d < min_distances[nei]:
                        min_distances[nei] = w + curr_d
                        heappush(heap, (w+curr_d, nei))
            return min_distances[end]
        
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            if w != -1:
                adj[a].append((b, w))
                adj[b].append((a, w))
        
        curr_dist = dijkstra(source, destination, adj)
        if curr_dist < target:
            return []
        if curr_dist == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges
        
        for i, (a, b, w) in enumerate(edges):
            if w != -1:
                continue
            edges[i][2] = 1
            adj[a].append((b, 1))
            adj[b].append((a, 1))
            
            dist = dijkstra(source, destination, adj)
            if dist <= target:
                edges[i][2] += target - dist
                for j in range(i+1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges
        return []