'''
Find K Closest Elements

Solution
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
#my try, accepted
# class Solution:
#     def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
#         l, r = 0, len(arr)-1
#         while l<r:
#           mid = l + ((r-l)>>1)
#           if arr[mid] < x:
#               l = mid + 1
#           else:
#               r = mid

#         res = []
#         i = l-1
#         j = l
#         for _ in range(k):
#           print(res, i, j)
#           if i>=0 and j<len(arr):
#               if abs(arr[i] - x) < abs(arr[j] - x):
#                   res.append(arr[i])
#                   i -= 1
#               elif abs(arr[i] - x) > abs(arr[j] - x):
#                   res.append(arr[j])
#                   j += 1
#               else:
#                   if arr[i]<arr[j]:
#                       res.append(arr[i])
#                       i -= 1
#                   else:
#                       res.append(arr[j])
#                       j += 1

#           elif i<0:
#               res.append(arr[j])
#               j += 1
#           else:
#               res.append(arr[i])
#               i -= 1
#         res.sort()
#         return res

#from leetcode solution, custom comparator O(nlogn+klogk)
# class Solution:
#     def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
#         # Sort using custom comparator
#         sorted_arr = sorted(arr, key = lambda num: abs(x - num))
#         print(sorted_arr)
#         # Only take k elements
#         result = []
#         for i in range(k):
#             result.append(sorted_arr[i])
        
#         # Sort again to have output in ascending order
#         return sorted(result)

# from leetcode Solution O(log(n-k)) Approach 3: Binary Search To Find The Left Bound
class Solution:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        if len(arr) == k:
            return arr
        l, r = 0, len(arr)-k
        while l<r:
            mid = l + (r-l)//2
            print(l, r, mid)
            # if abs(x-arr[mid]) > abs(x-arr[mid+k]): dont use this, fails in conditions like [1, 1, 2, 2, 2, 2, 2, 3, 3]
            if x - arr[mid] > arr[mid+k] - x:
                l = mid + 1
            else:
                r = mid
        # print(l, r)
        return arr[l:l+k]

arr = [1,2,3,4,5]
k = 4
x = 3
# Output: [1,2,3,4]

arr = [1,2,3,4,5]
k = 4
x = -1
# Output: [1,2,3,4]

arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
# # Real Expected: [3,3,4]

arr = [1,1,2,2,2,2,2,3,3]
x = 3
k = 3
# Output: [2, 3, 3]

s = Solution()
print(s.findClosestElements(arr, k, x))
