'''
3510. Minimum Pair Removal to Sort Array II
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:

Input: nums = [5,2,3,1]

Output: 2

Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]

Output: 0

Explanation:

The array nums is already sorted.

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        next = [i+1 for i in range(n)]
        prev = [i-1 for i in range(n)]
        removed = [False]*n
        vals = [nums[i] for i in range(n)]
        inversions = sum(1 if (nums[i] > nums[i+1]) else 0 for i in range(n-1))
        pq = [(nums[i] + nums[i+1], i) for i in range(n-1)]
        heapify(pq)

        def merge(i):
            nonlocal inversions
            if next[i] == n:
                return
            j = next[i]
            y = next[j]
            x = prev[i]

            if x != -1 and vals[x] > vals[i]: inversions -= 1
            if y != n and vals[j] > vals[y]: inversions -= 1
            if vals[i] > vals[j]: inversions -= 1

            vals[i] += vals[j]
            if x != -1 and vals[x] > vals[i]: inversions += 1
            if y != n and vals[i] > vals[y]: inversions += 1
            removed[j] = True
            next[i] = y
            if y != n:
                prev[y] = i
                heappush(pq, (vals[i]+vals[y], i))
            if x != -1:
                heappush(pq, (vals[x]+vals[i], x))

        def top_element():
            while pq:
                s, i = pq[0]
                if removed[i] or next[i] == n or s != vals[i] + vals[next[i]]:
                    heappop(pq)
                    continue
                else:
                    break
            if not pq:
                return -1
            return pq[0][1]

        ops = 0
        while inversions != 0:
            i = top_element()
            merge(i)
            ops += 1

        return ops
