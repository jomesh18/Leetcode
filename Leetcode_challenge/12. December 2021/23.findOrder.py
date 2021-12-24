'''
210. Course Schedule II
Medium

5487

208

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
Accepted
526,565
Submissions
1,160,222
'''
from collections import defaultdict
# class Solution:

#     WHITE = 1
#     GRAY = 2
#     BLACK = 3
#    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: List[int]
#         """

#         # Create the adjacency list representation of the graph
#         adj_list = defaultdict(list)

#         # A pair [a, b] in the input represents edge from b --> a
#         for dest, src in prerequisites:
#             adj_list[src].append(dest)

#         topological_sorted_order = []
#         is_possible = True

#         # By default all vertces are WHITE
#         color = {k: Solution.WHITE for k in range(numCourses)}
#         def dfs(node):
#             nonlocal is_possible

#             # Don't recurse further if we found a cycle already
#             if not is_possible:
#                 return

#             # Start the recursion
#             color[node] = Solution.GRAY

#             # Traverse on neighboring vertices
#             if node in adj_list:
#                 for neighbor in adj_list[node]:
#                     if color[neighbor] == Solution.WHITE:
#                         dfs(neighbor)
#                     elif color[neighbor] == Solution.GRAY:
#                          # An edge to a GRAY vertex represents a cycle
#                         is_possible = False

#             # Recursion ends. We mark it as black
#             color[node] = Solution.BLACK
#             topological_sorted_order.append(node)

#         for vertex in range(numCourses):
#             # If the node is unprocessed, then call dfs on it.
#             if color[vertex] == Solution.WHITE:
#                 dfs(vertex)

#         return topological_sorted_order[::-1] if is_possible else []


#my try of above
class Solution:
    WHITE = 0
    GRAY = 1
    BLACK = 2
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        adj_list = defaultdict(list)
        for end, start in prerequisites:
            adj_list[start].append(end)

        color = {k: Solution.WHITE for k in range(numCourses)}
        topological_sorted_order = []
        is_possible = True

        def dfs(vertex):
            nonlocal is_possible
            if not is_possible:
                return
            color[vertex] = Solution.GRAY
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        is_possible = False
                        return
            color[vertex] = Solution.BLACK
            topological_sorted_order.append(vertex)

        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []

numCourses = 2
prerequisites = [[1,0]]
# Output: [0,1]

# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]

# numCourses = 1
# prerequisites = []
# Output: [0]

sol = Solution()
print(sol.findOrder(numCourses, prerequisites))
