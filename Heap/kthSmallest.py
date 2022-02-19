'''
378. Kth Smallest Element in a Sorted Matrix
Medium

5396

227

Add to List

Share
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
Accepted
359,128
Submissions
606,442
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        heapq.heapify(heap)
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heap[0]

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minheap = []
        for i in range(min(k, n)):
            minheap.append((matrix[i][0], i, 0))
        heapq.heapify(minheap)
        ans = -1
        for i in range(k):
            ans, r, c = heapq.heappop(minheap)
            if c+1 < n: heapq.heappush(minheap, (matrix[r][c+1], r, c+1))
        return ans

#binary search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def elems_lt(mid):
            count = 0
            c = n-1
            for r in range(n):
                while c >=0 and matrix[r][c] > mid: c -= 1
                count += (c+1)
            return count

        lo, hi = matrix[0][0], matrix[n-1][n-1]

        while lo < hi:
            mid = lo + ((hi-lo)>>1)
            if elems_lt(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo