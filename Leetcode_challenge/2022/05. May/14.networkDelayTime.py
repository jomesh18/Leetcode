'''
743. Network Delay Time
Medium

4807

305

Add to List

Share
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
Accepted
276,149
Submissions
551,359

'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for s, d, t in times:
            g[s].append((t, d))
        min_heap = [(0, k)]

        distance = [float("inf")]*(n+1)
        distance[0], distance[k] = 0, 0
        visited = set()
        while min_heap and len(visited) != n:
            d, nod = heappop(min_heap)
            if nod in visited: continue
            visited.add(nod)
            for dist, node in g[nod]:
                if dist+d < distance[node]:
                    distance[node] = d+dist
                    heappush(min_heap, (d+dist, node))
        ans = max(distance)
        return ans if ans != float("inf") else -1