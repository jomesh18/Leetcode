'''
658. Find K Closest Elements
Medium

5432

478

Add to List

Share
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for v in arr:
            heappush(heap, (-abs(v-x), -v))
            if len(heap) > k:
                heappop(heap)
        return sorted([-v for _, v in heap])


#O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        while r-l >= k:
            if x-arr[l] <= arr[r] - x:
                r -= 1
            else:
                l += 1
        return arr[l:r+1]

# O(log(n-k))
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-k
        while l < r:
            mid = (l+r)//2
            if x-arr[mid] > arr[mid+k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l+k]