'''
1200. Minimum Absolute Difference
Easy

1087

48

Add to List

Share
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
Accepted
92,362
Submissions
133,645
'''
#O(nlogn)
# class Solution:
#     def minimumAbsDifference(self, arr: [int]) -> [[int]]:
#         arr.sort()
#         ans = []
#         min_ = float("inf")
#         for i in range(len(arr)-1):
#             diff = arr[i+1] - arr[i]
#             if diff < min_:
#                 ans = [[arr[i], arr[i+1]]]
#                 min_ = diff
#             elif diff == min_:
#                 ans.append([arr[i], arr[i+1]])
#         return ans

#O(m+n) Counting sort
class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        min_ = min(arr)
        max_ = max(arr)
        line = [0] *((max_-min_)+1)
        offset = -min_
        for num in arr:
            line[num+offset] = 1
        min_diff = float("inf")
        prev, curr = 0, None
        ans = []
        for i in range(1, len(line)):
            if line[i]:
                curr = i
                diff = curr-prev
                if diff < min_diff:
                    ans = [[prev-offset, curr-offset]]
                    min_diff = diff
                elif diff == min_diff:
                    ans.append([prev-offset, curr-offset])
                prev = curr
        return ans


arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]

arr = [1,3,6,10,15]
# # # # Output: [[1,3]]

# arr = [3,8,-10,23,19,-4,-14,27]
# # Output: [[-14,-10],[19,23],[23,27]]

sol = Solution()
print(sol.minimumAbsDifference(arr))
