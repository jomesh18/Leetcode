'''

Code

Testcase
Test Result
Test Result

815. Bus Routes
Solved
Hard
Topics
Companies
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
'''
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        bus_route = defaultdict(list)
        stop_bus = defaultdict(set)
        q = []
        visited = set()
        for bus, route in enumerate(routes):
            bus_route[bus] = set(route)
            if source in bus_route[bus]:
                q.append(bus)
                if target in bus_route[bus]:
                    return 1
                visited.add(bus)
            for stop in route:
                stop_bus[stop].add(bus)
        ans = 1
        while q:
            nq = []
            for bus in q:
                if target in bus_route[bus]:
                    return ans
                for stop in bus_route[bus]:
                    for next_bus in stop_bus[stop]:
                        if next_bus != bus and next_bus not in visited:
                            visited.add(next_bus)
                            nq.append(next_bus)
            q = nq
            ans += 1
        return -1