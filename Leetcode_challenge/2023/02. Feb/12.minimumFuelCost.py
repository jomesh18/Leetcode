'''
2477. Minimum Fuel Cost to Report to the Capital
Medium

1529

58

Add to List

Share
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.

 

Example 1:


Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation: 
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum. 
It can be proven that 3 is the minimum number of liters of fuel needed.
Example 2:


Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
Output: 7
Explanation: 
- Representative2 goes directly to city 3 with 1 liter of fuel.
- Representative2 and representative3 go together to city 1 with 1 liter of fuel.
- Representative2 and representative3 go together to the capital with 1 liter of fuel.
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative5 goes directly to the capital with 1 liter of fuel.
- Representative6 goes directly to city 4 with 1 liter of fuel.
- Representative4 and representative6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum. 
It can be proven that 7 is the minimum number of liters of fuel needed.
Example 3:


Input: roads = [], seats = 1
Output: 0
Explanation: No representatives need to travel to the capital city.
 

Constraints:

1 <= n <= 105
roads.length == n - 1
roads[i].length == 2
0 <= ai, bi < n
ai != bi
roads represents a valid tree.
1 <= seats <= 105
'''
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = [[] for _ in range(len(roads)+1)]
        for s, d in roads:
            adj[s].append(d)
            adj[d].append(s)
        self.ans = 0
        def dfs(node, parent, passengers, cars):
            ans = 0
            for nei in adj[node]:
                if nei != parent:
                    tc, tp, tf = dfs(nei, node, 1, 1)
                    cars += tc
                    passengers += tp
                    self.ans += tf
            cars = ceil(passengers / seats)
            
            return cars, passengers, cars

        dfs(0, -1, 0, 0)
        return self.ans

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = [[] for _ in range(len(roads)+1)]
        for s, d in roads:
            adj[s].append(d)
            adj[d].append(s)
        self.fuel = 0
        def dfs(node, parent):
            reps = 1
            for nei in adj[node]:
                if nei != parent:
                    reps += dfs(nei, node)
            if node != 0:
                self.fuel += ceil(reps/seats)
            return reps

        dfs(0, -1)
        return self.fuel

# bfs
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = [[] for _ in range(n)]
        degree = [0]*n
        for s, d in roads:
            adj[s].append(d)
            adj[d].append(s)
            degree[s] += 1
            degree[d] += 1
        reps = [1]*n  
        fuel = 0
        q = []
        for i in range(1, n):
            if degree[i] == 1:
                q.append(i)
        while q:
            new_q = []
            for node in q:
                fuel += ceil(reps[node]/seats)
                for nei in adj[node]:
                    degree[nei] -= 1
                    reps[nei] += reps[node]
                    if degree[nei] == 1 and nei != 0:
                        new_q.append(nei)
            q = new_q
        return fuel