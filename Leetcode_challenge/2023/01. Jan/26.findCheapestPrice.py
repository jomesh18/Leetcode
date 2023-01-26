'''
787. Cheapest Flights Within K Stops
Medium

6655

300

Add to List

Share
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s, d, c in flights:
            adj[s].append((d, c))
        # print(adj)
        ans = float('inf')
        q = {node: cost for node, cost in adj[src]}
        level = k + 1
        while q and level:
            tq = {}
            for node, cost in q.items():
                if node == dst:
                    ans = min(ans, cost)
                    continue
                for child, c in adj[node]:
                    tq[child] = min(tq.get(child, float('inf')), cost+c)

            q = tq
            level -= 1

        return ans if ans != float('inf') else -1

#bfs
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s, d, c in flights:
            adj[s].append((d, c))
        dist = [float('inf')]*n
        q = [(src, 0)]
        level = k+1
        while q and level:
            tq = []
            for node, cost in q:
                for nei, c in adj[node]:
                    if dist[nei] > cost + c:
                        dist[nei] = cost + c
                        tq.append((nei, dist[nei]))
            q = tq
            level -= 1
        return dist[dst] if dist[dst] != float('inf') else -1


# dijkstra's algo
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s, d, c in flights:
            adj[s].append((c, d))
        stops = [float('inf')]*n
        heap = [(0, src, 0)]
        while heap:
            cost, curr, count = heappop(heap)
            if count > stops[curr] or count > k+1: continue
            stops[curr] = count
            if curr == dst: return cost
            for c, nei in adj[curr]:
                heappush(heap, (cost+c, nei, count+1))
        return -1


# bellman ford
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')]*n
        dist[src] = 0
        for _ in range(k+1):
            t = dist.copy()
            for s, d, c in flights:
                if dist[s] != float('inf'):
                    t[d] = min(t[d], dist[s] + c)
            dist = t

        return dist[dst] if dist[dst] != float('inf') else -1