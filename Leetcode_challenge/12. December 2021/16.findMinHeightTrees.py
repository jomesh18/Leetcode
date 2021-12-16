'''
310. Minimum Height Trees
Medium

4262

172

Add to List

Share
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Example 3:

Input: n = 1, edges = []
Output: [0]
Example 4:

Input: n = 2, edges = [[0,1]]
Output: [0,1]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
Accepted
164,425
Submissions
447,382
'''
#using Topological Sort
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: [[int]]) -> [int]:
#         if n <= 2: return [i for i in range(n)]

#         neighbors = [set() for _ in range(n)]

#         for start, end in edges:
#             neighbors[start].add(end)
#             neighbors[end].add(start)


#         leaves = []

#         for i in range(n):
#             if len(neighbors[i]) == 1:
#                 leaves.append(i)

#         nodes_remaining = n

#         while nodes_remaining > 2:
#             nodes_remaining -= len(leaves)
#             new_leaves = []
#             while leaves:
#                 leaf = leaves.pop()
#                 neighbor = neighbors[leaf].pop()
#                 neighbors[neighbor].remove(leaf)
#                 if len(neighbors[neighbor]) == 1:
#                     new_leaves.append(neighbor)
#             leaves = new_leaves

#         return leaves

#using two dfs
class Solution:
    def findMinHeightTrees(self, n: int, edges: [[int]]) -> [int]:
        self.seen = set()
        def dfs(i):
            longestPath, path = [], []
            self.seen.add(i)
            for adj in g[i]:
                if adj not in self.seen:
                    path = dfs(adj)
                    if len(path) > len(longestPath):
                        longestPath = path[:]
            self.seen.remove(i)
            longestPath.append(i)
            return longestPath

        g = [set() for i in range(n)]

        for start, end in edges:
            g[start].add(end)
            g[end].add(start)

        path = dfs(0)
        print(path)
        leaf = path[0]
        ans = dfs(leaf)
        print(ans)
        if len(ans) & 1:
            return [ans[len(ans)//2]]
        return [ans[len(ans)//2], ans[(len(ans)//2)-1]]


n = 4
edges = [[1,0],[1,2],[1,3]]
# Output: [1]

# n = 6
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# # Output: [3,4]

# n = 1
# edges = []
# # Output: [0]

# n = 2
# edges = [[0,1]]
# # Output: [0,1]

sol = Solution()
print(sol.findMinHeightTrees(n, edges))
