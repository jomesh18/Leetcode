'''
Longest Turbulent Subarray

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

    For i <= k < j:
        arr[k] > arr[k + 1] when k is odd, and
        arr[k] < arr[k + 1] when k is even.
    Or, for i <= k < j:
        arr[k] > arr[k + 1] when k is even, and
        arr[k] < arr[k + 1] when k is odd.

 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

Example 2:

Input: arr = [4,8,12,16]
Output: 2

Example 3:

Input: arr = [100]
Output: 1

Constraints:

    1 <= arr.length <= 4 * 104
    0 <= arr[i] <= 109

'''
# my try
# class Solution:
#     def maxTurbulenceSize(self, arr: [int]) -> int:
#         if len(arr) == 1: return 1
#         i = 0
#         size = 0
#         gt = 1
#         lt = 1
#         temp = 0
#         while i < len(arr)-1:
#             # print("i {}, gt {}, lt {}, temp {}, size {}".format(i, gt, lt, temp, size))
#             if arr[i] > arr[i+1]:
#                 if lt:
#                     temp += 1
#                 else:
#                     size = max(size, temp)
#                     temp = 1
#                 gt = 1
#                 lt = 0
#             elif arr[i] < arr[i+1]:
#                 if gt:
#                     temp += 1
#                 else:
#                     size = max(size, temp)
#                     temp = 1
#                 lt = 1
#                 gt = 0
#             else:
#                 gt, lt = 1, 1
#                 size = max(size, temp)
#                 temp = 0
#             i += 1
#         return max(size, temp) + 1

#from leetcode
class Solution:
    def maxTurbulenceSize(self, arr):
        N = len(arr)
        ans = 1
        anchor = 0
        def cmp(a, b):
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0

        for i in range(1, N):
            c = cmp(arr[i-1], arr[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * cmp(arr[i], arr[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans

arr = [9,4,2,10,7,8,8,1,9]
# Output: 5

arr = [4,8,12,16]
# # Output: 2

arr = [100]
# # Output: 1

# arr = [9,9]
# Output: 1

arr = [0,1,1,0,1,0,1,1,0,0]
# Output: 5

arr = [0,8,45,88,48,68,28,55,17,24]
# Output: 8

sol = Solution()
print(sol.maxTurbulenceSize(arr))
