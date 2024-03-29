'''
Course Schedule

Solution
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {i: set() for i in range(numCourses)}
        can_do = {i: set() for i in range(numCourses)}
        for a, b in prerequisites:
            reqs[a].add(b)
            can_do[b].add(a)
        q = []
        for i in range(numCourses):
            if len(reqs[i]) == 0:
                q.append(i)
        visited = set()
        while q:
            newq = []
            for i in q:
                visited.add(i)
                for j in can_do[i]:
                    reqs[j].remove(i)
                    if len(reqs[j]) == 0:
                        newq.append(j)
            q = newq
            
        return len(visited) == numCourses


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        can_do = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            indegree[a] += 1
            can_do[b].append(a)
        q = [i for i in range(numCourses) if indegree[i] == 0]
        visited = set()
        while q:
            newq = []
            for i in q:
                visited.add(i)
                for j in can_do[i]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        newq.append(j)
            q = newq
        return len(visited) == numCourses