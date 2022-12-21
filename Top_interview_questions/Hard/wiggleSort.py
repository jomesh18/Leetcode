'''
324. Wiggle Sort II
Medium

2516

869

Add to List

Share
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.
 

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        for i in range(1, len(nums), 2):
            nums[i] = arr.pop()
            
        for i in range(0, len(nums), 2):
            nums[i] = arr.pop()
        

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find median using quick select O(n) average time
        def find_med(l, r, k):
            while True:
                pivot_ind = random.randint(l, r)
                nums[pivot_ind], nums[r] = nums[r], nums[pivot_ind]
                store_ind = l
                for i in range(l, r):
                    if nums[i] < nums[r]:
                        nums[i], nums[store_ind] = nums[store_ind], nums[i]
                        store_ind += 1
                nums[store_ind], nums[r] = nums[r], nums[store_ind]
                if store_ind < k:
                    l = store_ind + 1
                elif store_ind > k:
                    r = store_ind - 1
                else: return store_ind

        n = len(nums)
        median_ind = (n-1)//2
        median = nums[find_med(0, n-1, median_ind)]
        print(nums, median)
        odd = 1
        even = n-1 if (n & 1) else n-2
        
        # 3 color sort (Dutch national flag problem) higher on left, lower on right of median
        temp = [0]*n
        for j in range(n):
            if nums[j] > median:
                temp[odd] = nums[j]
                odd += 2
            elif nums[j] < median:
                temp[even] = nums[j]
                even -= 2
        while odd < n:
            temp[odd] = median
            odd += 2
        while even >= 0:
            temp[even] = median
            even -= 2
        for i in range(n):
            nums[i] = temp[i]


# O(n) time, O(1) space
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def find_med(l, r, k):
            while True:
                pivot_ind = random.randint(l, r)
                nums[r], nums[pivot_ind] = nums[pivot_ind], nums[r]
                store_ind = l
                for i in range(l, r):
                    if nums[i] < nums[r]:
                        nums[store_ind], nums[i] = nums[i], nums[store_ind]
                        store_ind += 1
                nums[r], nums[store_ind] = nums[store_ind], nums[r]
                if store_ind == k:
                    return k
                elif store_ind < k:
                    l = store_ind + 1
                else:
                    r = store_ind - 1
        
        n = len(nums)
        med_ind = (n-1)//2
        # rearranging median to correct position using quick select O(n) average case
        find_med(0, n-1, med_ind)
        
        median = nums[med_ind]
        
        new_idx = lambda i: (2*i+1)%(n|1)
        i, j, k = 0, 0, n-1
        while j <= k:
            if nums[new_idx(j)] > median:
                nums[new_idx(i)], nums[new_idx(j)] = nums[new_idx(j)], nums[new_idx(i)]
                i += 1
                j += 1
            elif nums[new_idx(j)] < median:
                nums[new_idx(k)], nums[new_idx(j)] = nums[new_idx(j)], nums[new_idx(k)]
                k -= 1
            else:
                j += 1
        