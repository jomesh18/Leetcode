'''
 Keys and Rooms

Solution
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
'''

# my try
# class Solution:
#     def canVisitAllRooms(self, rooms: [[int]]) -> bool:
#         visited = [False]*len(rooms)
#         def dfs(room):
#         	if not visited[room]:
# 	        	visited[room] = True
# 	        	for key in rooms[room]:
# 	        		if not visited[key]:
# 	        			dfs(key)
#         dfs(0)
#         return all(visited)

# my try again, using set
# class Solution:
#     def canVisitAllRooms(self, rooms: [[int]]) -> bool:
#         visited = set()
#         def dfs(room):
#         	if room not in visited:
# 	        	visited.add(room)
# 	        	for key in rooms[room]:
# 	        		if key not in visited:
# 	        			dfs(key)
#         dfs(0)
#         return len(visited) == len(rooms)

# my try, using bfs
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: [[int]]) -> bool:
        visited = set()
        def bfs(room):
        	q = deque([(room)])
        	while q:
	        	c = q.popleft()
	        	if c not in visited:
		        	visited.add(c)
		        	if len(visited) == len(rooms):
		        		return True
		        	for key in rooms[c]:
		        		if key not in visited:
		        			q.append((key))
        return bfs(0)

rooms = [[1],[2],[3],[]]
# Output: true

# rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false

s = Solution()
print(s.canVisitAllRooms(rooms))
