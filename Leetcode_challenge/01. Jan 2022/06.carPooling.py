'''
1094. Car Pooling
Medium

2207

55

Add to List

Share
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 

Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
Accepted
111,065
Submissions
186,785
'''
# O(nlogn)
class Solution:
    def carPooling(self, trips: [[int]], capacity: int) -> bool:
        new_trips = []
        for n, entry, exit in trips:
            new_trips.extend([(entry, 1, n), (exit, 0, n)])
        # new_trips.sort(key= lambda x: (x[0], x[2]))
        new_trips.sort()
        # print(new_trips)
        for pos, n, status in new_trips:
            if status:
                capacity -= n
                if capacity < 0: return False
            else:
                capacity += n
        return True

#O(n)
class Solution:
    def carPooling(self, trips: [[int]], capacity: int) -> bool:
        stops = [0] * 1001
        for n, entry, exit in trips:
            stops[entry] += n
            stops[exit] -= n
        # print(stops)
        passengers = 0
        for stop in stops:
            passengers += stop
            if passengers > capacity: return False
        return True

trips = [[2,1,5],[3,3,7]]
capacity = 4
# Output: false

# trips = [[2,1,5],[3,3,7]]
# capacity = 5
# Output: true

trips = [[2,1,5], [3,5,7]]
capacity = 3

sol = Solution()
print(sol.carPooling(trips, capacity))
