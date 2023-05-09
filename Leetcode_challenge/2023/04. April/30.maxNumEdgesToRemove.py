'''
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Hard

1783

27

Add to List

Share
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
'''
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class UF:
            def __init__(self, n):
                self.root = [i for i in range(n+1)]
                self.rank = [1]*(n+1)
                self.components = n
            
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                
                if px != py:
                    if self.rank[px] > self.rank[py]:
                        self.root[py] = px
                    else:
                        self.root[px] = py
                        if self.rank[px] == self.rank[py]:
                            self.rank[py] += 1
                    self.components -= 1
                    return True
                return False
        
        uf1 = UF(n)
        uf2 = UF(n)
        a = []
        b = []
        ab = []
        required = 0
        for e in edges:
            if e[0] == 3:
                ab.append(e)
            elif e[0] == 2:
                b.append(e)
            else:
                a.append(e)

        for _, f, t in ab:
            req = uf1.union(f, t)
            req |= uf2.union(f, t)
            if req:
                required += 1
            
        for _, f, t in a:
            if uf1.union(f, t):
                required += 1
        for _, f, t in b:
            if uf2.union(f, t):
                required += 1

        return -1 if (uf1.components != 1 or uf2.components != 1) else len(edges)-required