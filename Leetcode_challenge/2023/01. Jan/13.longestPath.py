'''
2246. Longest Path With Different Adjacent Characters
Hard

2036

53

Add to List

Share
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

 

Example 1:


Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
Example 2:


Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
 

Constraints:

n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.
'''
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[i].append(parent[i])
            adj[parent[i]].append(i)
        
        # print(adj)
        self.ans = 0
        def dfs(node, parent=None):
            curr_c = s[node]
            curr_l = 1
            t = []
            for nei in adj[node]:
                if nei != parent:
                    l, c = dfs(nei, node)
                    if c != curr_c:
                        if len(t) < 2:
                            t.append(l)
                        elif l > min(t):
                            t = [max(t), l]
                # print(node, t)
            l1, l2 = 0, 0
            if t:
                l1 = t.pop()
            if t:
                l2 = t.pop()
            self.ans = max(self.ans, curr_l+l1+l2)
            return (curr_l+max(l1, l2), curr_c)
            
        dfs(0)
        return self.ans


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        
        # print(children)
        self.ans = 0
        def dfs(node):
            candidates = []
            for child in children[node]:
                l = dfs(child)
                if s[node] != s[child]:
                    if len(candidates) < 2:
                        candidates.append(l)
                    elif l > min(candidates):
                        candidates = [max(candidates), l]
            self.ans = max(self.ans, sum(candidates)+1)
            return 1+ (max(candidates) if candidates else 0)
            
        dfs(0)
        return self.ans