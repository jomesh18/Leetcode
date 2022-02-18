'''
347. Top K Frequent Elements
Medium

7397

327

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

Accepted
812,582
Submissions
1,261,727
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        l = []
        count = 0
        for key in d.copy():
            if count < k:
                l.append((d[key], key))
                count += 1
                del d[key]
        heapq.heapify(l)
        for key in d:
            if d[key] > l[0][0]:
                heapq.heapreplace(l, (d[key], key))
        res = []
        while l:
            res.append(heapq.heappop(l)[1])
        return res
        