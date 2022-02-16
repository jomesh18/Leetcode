'''
Evaluate Division

Solution
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
'''
# using bfs/dfs and as graph
# from collections import defaultdict, deque
# class Solution:
#     def calcEquation(self, equations: [[str]], values: [float], queries: [[str]]) -> [float]:
#         G = defaultdict(dict)

#         for (x, y), v in zip(equations, values):
#             G[x][y] = v
#             G[y][x] = 1/v

#         def bfs(src, dst):
#             if src not in G or dst not in G: return -1.0

#             q, seen = [(src, 1.0)], set()

#             for x, val in q:
#                 if x == dst: return val
#                 seen.add(x)
#                 for y in G[x]:
#                     if y not in seen:
#                         q.append((y, G[x][y]*val))
#             return -1.0
#         return [bfs(src, dst) for src, dst in queries]

#Union Find
'''
public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        double[] res = new double[queries.size()];
        UF uf = new UF();
        for (int i = 0; i < values.length ; ++i )
            uf.union(equations.get(i).get(0), equations.get(i).get(1), values[i]);
        for (int i = 0; i < queries.size(); ++i) {
            String x = queries.get(i).get(0), y = queries.get(i).get(1);
            res[i] = (uf.parents.containsKey(x) && uf.parents.containsKey(y) && uf.find(x) == uf.find(y)) ? uf.vals.get(x) / uf.vals.get(y) : -1.0;
        }
        return res;
    }
    
    class UF {
        /**
         * parents: (x, root(x)), vals:(x, x/root(x)), for example, a / b = 2.0, we will have parents(a, b), vals(a, 2.0), both parents and vals have the numerator (which is 'a' here)
         * so that we can search for it and get the value a / parents(a) = vals.get(a) which is a / b = 2.0.
         */
        Map<String, String> parents;
        Map<String, Double> vals;
        UF() {
            parents = new HashMap<>();
            vals = new HashMap<>();
        }
        
        public void add(String x) {
            if (parents.containsKey(x)) return;
            parents.put(x, x);
            vals.put(x, 1.0);
        }

        /**
         * find the root
         * parents(x, p) = vals(x), x / p = vals(x), parents(p, pp) = vals(p), p / pp = vals(pp), when we are looking for the root, we are doing a path compression here
         * parents(x, pp)  = vals(x) / vals(pp) =  (x / p) * (p / pp) = vals(x) * vals(p)
         * For example, a / b = 2.0, b / c = 3.0,  parents(a, b) = 2.0,  parents(b, c) = 3.0, parents(a, c) = 2.0 * 3.0 = 6.0, now vals(a) = 6.0
         * So along the way, we get all the value of a / x where x is the parent of x all the way to root. In the end, only a / root(x) is saved. This is path compression.
         * It's like putting a directly under the root(x)
         */
        public String find(String x) {
            String p = parents.getOrDefault(x, x);
            if (x != p) {
                String pp = find(p);
                vals.put(x, vals.get(x) * vals.get(p));
                parents.put(x, pp);
            }
            return parents.getOrDefault(x, x);
        }

        /**
         * x / px = vals.get(x), y / py = vals.get(y), so px / py =  v * vals.get(y) / vals.get(x)
         */
        public void union(String x, String y, double v) {
            add(x); add(y);
            String px = find(x), py = find(y);
            parents.put(px, py);
            vals.put(px, v * vals.get(y) / vals.get(x));
        }

    }
'''
class Solution:
    def calcEquation(self, equations: [[str]], values: [float], queries: [[str]]) -> [float]:

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


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

# equations = [["a","b"],["b","c"],["bc","cd"]]
# values = [1.5,2.5,5.0]
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# # Output: [3.75000,0.40000,5.00000,0.20000]

# equations = [["a","b"]]
# values = [0.5]
# queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# # Output: [0.50000,2.00000,-1.00000,-1.00000]

sol = Solution()
print(sol.calcEquation(equations, values, queries))
