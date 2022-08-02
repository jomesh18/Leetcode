'''
378. Kth Smallest Element in a Sorted Matrix
Medium

6851

253

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
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heappush(heap, -matrix[i][j])
                elif -matrix[i][j] >= heap[0]:
                    heappushpop(heap, -matrix[i][j])
        return -heap[0]

#using min heap and sorted property (min among n sorted rows)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(min(k, n)):
            heappush(heap, (matrix[i][0], i, 0))
        ans = -1
        for i in range(k):
            ans, r, c = heappop(heap)
            if c+1 < n: heappush(heap, (matrix[r][c+1], r, c+1))
        return ans

#binary search between lowest value and largest value
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def countLessOrEqual(x):
            c = n-1
            cnt = 0
            for r in range(n):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1
                cnt += c+1
            return cnt
        
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo+hi)//2
            if countLessOrEqual(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo