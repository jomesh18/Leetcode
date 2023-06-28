'''
1514. Path with Maximum Probability
Medium

2191

42

Add to List

Share
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
 

Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
'''
#bfs
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = [[] for _ in range(n)]
        for i, (v1, v2) in enumerate(edges):
            g[v1].append((v2, succProb[i]))
            g[v2].append((v1, succProb[i]))

        memo = [0]*n
        q = {start: 1}
        while q:
            nq = {}
            # print(q)
            for node, curr_p in q.items():
                if node == end:
                    memo[end] = max(memo[end], curr_p)
                    continue
                for nei, p in g[node]:
                    if p*curr_p > memo[nei]:
                        memo[nei] = p*curr_p
                        nq[nei] = p*curr_p
            q = nq
        return memo[end]

# dijkstra
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        probs = [0]*n
        probs[start] = 1
        max_heap = [(-probs[i], i) for i in range(n)]
        heapify(max_heap)
        g = [[] for _ in range(n)]
        for i, (v1, v2) in enumerate(edges):
            g[v1].append((v2, succProb[i]))
            g[v2].append((v1, succProb[i]))
            
        while max_heap:
            curr_p, i = heappop(max_heap)
            if i == end:
                return -curr_p
            for nei, p in g[i]:
                if probs[nei] < p*-curr_p:
                    probs[nei] = p*-curr_p
                    heappush(max_heap, (-probs[nei], nei))
        return 0

# bellman ford
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        probs = [0]*n
        probs[start] = 1
        e = []
        for k, (i, j) in enumerate(edges):
            e.extend([(i, j, succProb[k]), (j, i, succProb[k])])
        # print(e)
        while n > 1:
            n -= 1
            changes = 0
            for i, j, p in e:
                if probs[i]*p > probs[j]:
                    changes += 1
                    probs[j] = probs[i]*p
            if not changes:
                break
        return probs[end]