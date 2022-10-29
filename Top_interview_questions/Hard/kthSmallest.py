'''
Kth Smallest Element in a Sorted Matrix

Solution
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
# (n+n)*log(d), where d is the difference between biggest and smallest in matrix
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def lteq(num):
            row, col = 0, n-1
            c = 0
            while col >= 0 and row < n:
                if matrix[row][col] > num:
                    col -= 1
                elif matrix[row][col] <= num:
                    row += 1
                    c += (col+1)
            return c
                
        
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo+hi)//2
            if lteq(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

# klogk
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(min(n, k)):
            heap.append((matrix[i][0], i, 0))
        for _ in range(k-1):
            val, row, col = heappop(heap)
            if col + 1 < n: heappush(heap, (matrix[row][col+1], row, col+1))
        return heappop(heap)[0]
