'''
315. Count of Smaller Numbers After Self
Hard

7670

208

Add to List

Share
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        res = SortedList()
        for i in range(n-1, -1, -1):
            j = res.bisect_left(nums[i])
            res.add(nums[i])
            ans[i] = j
            # print(res, j, i, ans)
        return ans

# mergesort
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            l, r = 0, 0
            elemslessthanleftinright = 0
            merged = []
            while l < len(left) and r < len(right):
                if left[l][0] > right[r][0]:
                    merged.append(right[r])
                    r += 1
                    elemslessthanleftinright += 1
                else:
                    res[left[l][1]] += elemslessthanleftinright
                    merged.append(left[l])
                    l += 1
            if l < len(left):
                for i in range(l, len(left)):
                    res[left[i][1]] += elemslessthanleftinright
                    merged.append(left[i])
            elif r < len(right):
                for i in range(r, len(right)):
                    merged.append(right[i])
            return merged
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        
        arr = [(num, i) for i, num in enumerate(nums)]
        res = [0]*len(arr)
        merge_sort(arr)
        return res