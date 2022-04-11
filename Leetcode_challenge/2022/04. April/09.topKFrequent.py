'''
347. Top K Frequent Elements
Medium

8779

360

Add to List

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
#O(n) bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for key, freq in d.items():
            bucket[freq].append(key)
        flattened = list(chain(*bucket))
        return flattened[len(flattened)-k: ]



#O(n) qucik select/Hoare's algorithm (O(n) best, O(n*n) worst case runtime)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        unique = list(d.keys())
        
        n = len(unique)
        
        def partition(left, right, pivot_index):
            pivot_freq = d[unique[pivot_index]]
            
            unique[right], unique[pivot_index] = unique[pivot_index], unique[right]
            
            index = left
            
            for i in range(left, right):
                if d[unique[i]] < pivot_freq:
                    unique[index], unique[i] = unique[i], unique[index]
                    index += 1
            
            unique[index], unique[right] = unique[right], unique[index]
            
            return index
        
        def quick_select(left, right, kthsmallest):
            if left == right: return
            pivot_index = random.randint(left, right)
            
            ind = partition(left, right, pivot_index)
            
            if ind == kthsmallest:
                return
            elif ind < kthsmallest:
                quick_select(ind+1, right, kthsmallest)
            else:
                quick_select(left, ind-1, kthsmallest)
        
        quick_select(0, n-1, n-k)
        return unique[n-k: ]
