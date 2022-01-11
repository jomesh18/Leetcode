'''
973. K Closest Points to Origin
Medium

4636

188

Add to List

Share
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
Accepted
641,908
Submissions
971,962
'''
# O(nlogn), using sorting
# class Solution:
#     def kClosest(self, points: [[int]], k: int) -> [[int]]:

#         l = [(x*x+y*y, x, y) for x, y in points]
#         l.sort()
#         return [[x, y] for _, x, y in l[:k]]


# #using heap, O(nlogk)
# class Solution:
#     def kClosest(self, points: [[int]], k: int) -> [[int]]:
#         def find_dist(point):
#             return point[0] * point[0] + point[1]*point[1]

#         heap = [(-find_dist(points[i]), i) for i in range(k)]
#         heapq.heapify(heap)
#         for i in range(k, len(points)):
#             dist = -find_dist(points[i])
#             if dist>heap[0][0]:
#                 heapq.heappushpop(heap, (dist, i))
#         print(heap)
#         return [points[i] for (_, i) in heap]


#using binary search, O(n) average, O(n*n) worst
# class Solution:
#     def kClosest(self, points: [[int]], k: int) -> [[int]]:
#         def find_dist(point):
#             x, y = point
#             return (x**2+y**2)**.5

#         def split_array(remaining, mid):
#             closer, farther = [], []
#             for i in remaining:
#                 if distances[i] > mid:
#                     farther.append(i)
#                 else:
#                     closer.append(i)
#             return [closer, farther]

#         distances = [find_dist(point) for point in points]
#         remaining = [i for i in range(len(points))]

#         closest = []
#         lo, hi = 0, max(distances)
#         while k:
#             mid = (lo + ((hi-lo)/2))
#             # print(mid, lo, hi)
#             closer, farther = split_array(remaining, mid)

#             if len(closer) <= k:
#                 closest.extend(closer)
#                 remaining = farther
#                 k -= len(closer)
#                 lo = mid
#             else:
#                 remaining = closer
#                 hi = mid
#         return [points[i] for i in closest]

#using quick select alogorithm O(n) average
class Solution:

    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        def choose_pivot(left, right):
            return points[left + (right-left)//2]

        def find_distance(point):
            return point[0]**2 + point[1]**2

        def quick_select(points, k):
            left, right = 0, len(points)-1
            pivot_index = len(points)
            while pivot_index != k:
                pivot_index = partition(left, right)
                if pivot_index < k:
                    left = pivot_index
                else:
                    right = pivot_index - 1

            return points[:k]

        def partition(left, right):
            pivot = choose_pivot(left, right)
            pivot_distance = find_distance(pivot)
            while left < right:
                if find_distance(points[left]) >= pivot_distance:
                    points[left], points[right] = points[right], points[left]
                    right -= 1
                else:
                    left += 1
            if find_distance(points[left]) < pivot_distance:
                left += 1
            return left

        return quick_select(points, k)


points = [[1,3],[-2,2]]
k = 1
# Output: [[-2,2]]

# points = [[3,3],[5,-1],[-2,4]]
# k = 2
# Output: [[3,3],[-2,4]]

sol = Solution()
print(sol.kClosest(points, k))
