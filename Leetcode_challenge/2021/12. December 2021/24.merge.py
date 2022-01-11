'''
56. Merge Intervals
Medium

10979

459

Add to List

Share
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Accepted
1,188,726
Submissions
2,720,323
'''
#using sorting
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if len(intervals)<= 1: return intervals
#         intervals.sort()
#         print(intervals)
#         res = []
#         i,  j = 0, 1
#         start, end = intervals[0]
#         while j < len(intervals):
#             if intervals[i][1] >= intervals[j][0]:
#                 start = min(start, intervals[i][0])
#                 end = max(intervals[i][1], intervals[j][1])
#                 if intervals[i][1] < intervals[j][1]:
#                     i = j
#                 j += 1
#             else:
#                 res.append([start, end])
#                 start, end = intervals[j]
#                 i = j
#                 j += 1
#         res.append([start, end])
#         return res


#using sorting, from leetcode
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         intervals.sort(key=lambda x: x[0])

#         merged = []
#         for interval in intervals:
#             # if the list of merged intervals is empty or if the current
#             # interval does not overlap with the previous, simply append it.
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#             # otherwise, there is overlap, so we merge the current and previous
#             # intervals.
#                 merged[-1][1] = max(merged[-1][1], interval[1])

#         return merged

#O(n*n)
from collections import defaultdict
class Solution:
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def buildGraph(self, intervals):
        graph = defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def mergeNodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def getComponents(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = defaultdict(list)

        def markComponentDFS(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                comp_number += 1

        return nodes_in_comp, comp_number


    def merge(self, intervals: [[int]]) -> [[int]]:
        graph = self.buildGraph(intervals)
        nodes_in_comp, number_of_comps = self.getComponents(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.mergeNodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]

#counting sort
# O(N+R) where R is the range of intervals determined by start value
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         def counting_sort():
#             ends, j = defaultdict(list), 0
#             for interval in intervals:
#                 ends[interval[0]].append(interval[1])
#             for i in range(max(intervals)[0]+1):
#                 for end in ends[i]:
#                     intervals[j] = [i, end]
#                     j += 1

#         counting_sort()

#         res = [intervals[0]]
#         for interval in intervals:
#             if res[-1][1] >= interval[0]:
#                 res[-1][1] = max(interval[1], res[-1][1])
#             else:
#                 res.append(interval)
#         return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# intervals = [[1,4],[4,5]]
# Output: [[1,5]]

sol = Solution()
print(sol.merge(intervals))
