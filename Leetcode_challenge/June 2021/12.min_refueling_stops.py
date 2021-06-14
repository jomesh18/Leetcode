'''
Minimum Number of Refueling Stops
A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: 
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 

Note:

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
'''
#my try, tle
# class Solution:
#     def minRefuelStops(self, target: int, startFuel: int, stations: [[int]]) -> int:
#         def helper(fuel, i, count):
#             # print("helper({}, {}, {})".format(fuel, i, count))
#             if target-fuel <= 0:
#                 return count
#             if i == len(stations) or fuel < stations[i][0]:
#                 return float("inf")
#             return min(helper(fuel+stations[i][1], i+1, count+1), helper(fuel, i+1, count))
#         ans = helper(startFuel, 0, 0)
#         return ans if ans != float("inf") else -1

import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: [[int]]) -> int:
        fuel, count = startFuel, 0
        heap = []
        i = 0
        while True:
            if fuel >= target:
                return count
            while i < len(stations) and fuel >= stations[i][0]:
                heapq.heappush(heap, (-stations[i][1], stations[i][0]))
                i += 1
            if heap:
                fuel -= heapq.heappop(heap)[0]
                count += 1
            else:
                return -1

# target = 1
# startFuel = 1
# stations = []
# Output: 0

# target = 100
# startFuel = 1
# stations = [[10,100]]
# # Output: -1

# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]
# # Output: 2

target = 1000000000
startFuel = 145267354
stations = [[32131797,142290934],[86397166,44642653],[99237057,56978680],[130019011,99649968],[154227249,90514223],[198652959,102942413],[272491487,108474929],[282220105,83721209],[302284128,43151624],[318501736,107636032],[359336452,73807027],[425903682,43078334],[447483572,53751173],[469840976,57311636],[472584505,57629539],[531147470,106487691],[611722638,111485731],[650472592,20105771],[692670691,141572192],[747847056,7972504],[800899205,106134661],[825649709,136473550],[880534339,72135820],[887048383,73776979],[967172408,58930710]]
# print(len(stations))

s = Solution()
print(s.minRefuelStops(target, startFuel,stations))
