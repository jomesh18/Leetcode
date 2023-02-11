'''
1129. Shortest Path with Alternating Colors
Medium

1970

96

Add to List

Share
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q = {(0, 0), (0, 1)}
        res = [-1]*(n)
        red = defaultdict(list)
        blue = defaultdict(list)
        for s, e in redEdges:
            red[s].append(e)
        for s, e in blueEdges:
            blue[s].append(e)
            
        level = 0
        visited = [[False]*n for _ in range(2)]
        while q:
            new_q = set()
            for v, c in q:
                if not visited[c][v]:
                    if res[v] == -1: res[v] = level
                    visited[c][v] = True
                    if c:
                        curr = red
                    else:
                        curr = blue
                    for nex in curr[v]:
                        new_q.add((nex, not c))
            level += 1
            q = new_q
        return res