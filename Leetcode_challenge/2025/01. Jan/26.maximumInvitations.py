'''
2127. Maximum Employees to Be Invited to a Meeting
Solved
Hard
Topics
Companies
Hint
A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

 

Example 1:


Input: favorite = [2,2,1,2]
Output: 3
Explanation:
The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3. 
Example 2:

Input: favorite = [1,2,0]
Output: 3
Explanation: 
Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
The seating arrangement will be the same as that in the figure given in example 1:
- Employee 0 will sit between employees 2 and 1.
- Employee 1 will sit between employees 0 and 2.
- Employee 2 will sit between employees 1 and 0.
The maximum number of employees that can be invited to the meeting is 3.
Example 3:


Input: favorite = [3,0,1,4,1]
Output: 4
Explanation:
The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.
 

Constraints:

n == favorite.length
2 <= n <= 105
0 <= favorite[i] <= n - 1
favorite[i] != i
'''
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        reversed_graph = [[] for _ in range(n)]
        for i in range(n):
            reversed_graph[favorite[i]].append(i)
        
        def bfs(i, v, r):
            q = deque([(i, 0)])
            max_d = 0
            while q:
                curr, d = q.popleft()
                for nex in r[curr]:
                    if nex in v:
                        continue
                    v.add(nex)
                    q.append((nex, d+1))
                    max_d = max(max_d, d+1)

            return max_d

        longest = 0
        two_cycle = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                visited_dist = {}
                curr = i
                d = 0
                while True:
                    if visited[curr]:
                        break
                    visited[curr] = True
                    visited_dist[curr] = d
                    d += 1
                    nex = favorite[curr]
                    if nex not in visited_dist:
                        curr = nex
                        continue
                    curr_dist = d - visited_dist[nex]
                    longest = max(longest, curr_dist)
                    if curr_dist == 2:
                        visited_nodes = { curr, nex}
                        left = bfs(curr, visited_nodes, reversed_graph)
                        right = bfs(nex, visited_nodes, reversed_graph)
                        two_cycle += 2+left+right
                    curr = nex
                        
        return max(longest, two_cycle)