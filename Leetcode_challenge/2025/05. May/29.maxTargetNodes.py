'''
3373. Maximize the Number of Target Nodes After Connecting Trees II
Solved
Hard
Topics
premium lock icon
Companies
Hint
There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

Output: [8,7,7,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 4 from the second tree.
For i = 2, connect node 2 from the first tree to node 7 from the second tree.
For i = 3, connect node 3 from the first tree to node 0 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]

Output: [3,6,6,6,6]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.


 

Constraints:

2 <= n, m <= 105
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
'''
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)
        for a, b in edges2:
            adj2[a].append(b)
            adj2[b].append(a)
        
        def dfs(node, color, colors, adj):
            if colors[node] != -1: return
            colors[node] = color
            for nei in adj[node]:
                if colors[nei] != -1: continue
                dfs(nei, 1-color, colors, adj)
            
        n1 = len(adj1)
        colors1 = [-1]*n1
        dfs(0, 0, colors1, adj1)
        evens1 = colors1.count(0)
        n2 = len(adj2)
        colors2 = [-1]*n2
        dfs(0, 0, colors2, adj2)
        evens2 = colors2.count(0)
        max_count = max(evens2, n2-evens2)

        ans = [max_count]*n1
        for i in range(n1):

            curr_count = (n1-evens1) if (colors1[i] & 1) else evens1
            ans[i] += curr_count
        return ans
