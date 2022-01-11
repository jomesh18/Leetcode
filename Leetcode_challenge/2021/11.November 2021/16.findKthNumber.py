'''
668. Kth Smallest Number in Multiplication Table
Hard

Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

 

Example 1:

Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

Example 2:

Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.

 

Constraints:

    1 <= m, n <= 3 * 104
    1 <= k <= m * n

Accepted
35,150
Submissions
70,957
'''
# naive way, O(m*n) to build table, O(mnln(mn)) to sort, tle
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        table = []
        for i in range(1, m+1):
            for j in range(1, n+1):
                table.append(i*j)
        print(table)
        table.sort()
        return table[k-1]

#using heap
import heapq
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l = [(i, i) for i in range(1, m+1)] # l contains (val, root) for each row, every row starting value is stored in heap
        heapq.heapify(l) #sorted, min heap
        for _ in range(k):
            val, root = heapq.heappop(l)
            nxt = val + root
            if nxt <= root*n:
                heapq.heappush(l, (nxt, root))
        return val

#binary search, O(m*log(m*n)) or O(min(m, n)*log(m*n))
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n: m, n = n, m
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x//i, n)
            return count >= k
        lo, hi = 1, m*n
        while lo < hi:
            mid = (lo+hi) >> 1
            if enough(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

m = 3
n = 3
k = 5
# Output: 3

m = 2
n = 3
k = 6
# Output: 6

m = 34
n = 42
k = 401
# Output: 126

sol = Solution()
print(sol.findKthNumber(m, n, k))
