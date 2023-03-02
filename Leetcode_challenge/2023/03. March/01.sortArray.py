'''
912. Sort an Array
Medium

3782

640

Add to List

Share
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''
# merge sort, O(nlogn), O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, m, r):
            i, j = l, m+1
            t = []
            while i <= m and j <= r:
                if nums[i] < nums[j]:
                    t.append(nums[i])
                    i += 1
                else:
                    t.append(nums[j])
                    j += 1
            while i <= m:
                t.append(nums[i])
                i += 1
            while j <= r:
                t.append(nums[j])
                j += 1
            for i in range(l, r+1):
                nums[i] = t[i-l]
                    
        def merge_sort(start, end):
            if end > start:
                mid = (start+end)//2
                merge_sort(start, mid)
                merge_sort(mid+1, end)
                merge(start, mid, end)
        
        merge_sort(0, len(nums)-1)
        return nums

# O(nlogn), O(logn)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n, i):
            largest = i
            left, right = 2*i+1, 2*i+2
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                heapify(n, largest)
                
        def heap_sort():
            n = len(nums)
            for i in range(n//2-1, -1, -1):
                heapify(n, i)
            for i in range(n-1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(i, 0)
        heap_sort()
        return nums

# counting sort O(n+k), O(n+k) where k is the range of values
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        delta = min(nums)
        max_ = max(nums)
        counts = [0]*(max_-delta+1)
        for num in nums:
            new = num-delta
            counts[new] += 1
        i = 0
        for j in range(len(counts)):
            if counts[j]:
                for k in range(i, i+counts[j]):
                    nums[k] = j+delta
                i += counts[j]
        return nums


# radix sort, O(w(n+k)), O(n+k) where k in the range of values and w is the maximum length of number in nums
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort(place, k=10):
            counts = [0]*k
            for num in nums:
                digit = (num // place) % 10
                counts[digit] += 1
            starting_ind = 0
            for i, c in enumerate(counts):
                counts[i] = starting_ind
                starting_ind += c
            sorted_list = [0]*len(nums)
            for num in nums:
                digit = (num // place) % 10
                sorted_list[counts[digit]] = num
                counts[digit] += 1
            for i, e in enumerate(sorted_list):
                nums[i] = e
        min_ = min(nums)
        nums = [num-min_ for num in nums]
        max_ = max(nums)
        place_value = 1
        while place_value <= max_:
            counting_sort(place_value)
            place_value *= 10
        nums = [num+min_ for num in nums]
        return nums