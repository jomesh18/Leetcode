'''
399. Evaluate Division
Medium

5672

472

Add to List

Share
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
Accepted
274.1K
Submissions
468K
'''
#bfs
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for (s, e), v in zip(equations, values):
            g[s].append((e, v))
            g[e].append((s, 1/v))
            
        def find(query):
            s, e = query
            if s not in g or e not in g: return -1.0
            q = [(s, 1)]
            visited = {s}
            while q:
                t = []
                for curr, p in q:
                    if curr == e: return p
                    for child, v in g[curr]:
                        if child not in visited:
                            visited.add(child)
                            t.append((child, v*p))
                q = t[:]
            return -1.0
            
        return [find(query) for query in queries]

#elegent bfs
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            G[x][y] = v
            G[y][x] = 1/v
        def bfs(src, dst):
            if not (src in G and dst in G): return -1.0
            q, seen = [(src, 1.0)], set()
            for x, v in q:
                if x == dst: 
                    return v
                seen.add(x)
                for y in G[x]:
                    if y not in seen: 
                        q.append((y, v*G[x][y]))
            return -1.0
        return [bfs(s, d) for s, d in queries]


#union find
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        class UF:
            def __init__(self, alphabets):
                self.parent = {c: c for c in alphabets}
                self.val = {c: 1 for c in alphabets}
                self.rank = {c: 1 for c in alphabets}
            
            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x], val = self.find(self.parent[x])
                    self.val[x] = self.val[x] * val
                return self.parent[x], self.val[x]

            def union(self, x, y, v):
                px, vx = self.find(x)
                py, vy = self.find(y)
                if px == py: return
                if self.rank[px] <= self.rank[py]:
                    self.parent[px] = self.parent[py]
                    self.val[px] = vy*v/vx
                    if self.rank[px] == self.rank[py]: self.rank[px] += 1
                else:
                    self.union(y, x, 1/v)

        alphabets = set(sum(equations, []))
        uf = UF(alphabets)
        for (x, y), v in zip(equations, values):
            uf.union(x, y, v)

        ans = []

        for x, y in queries:
            if x in alphabets and y in alphabets:
                px, vx = uf.find(x)
                py, vy = uf.find(y)
                if px != py: ans.append(-1.0)
                else: ans.append(vx/vy)
            else:
                ans.append(-1.0)

        return ans