'''
Top K Frequent Elements

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
# class Solution:
#     def topKFrequent(self, nums: [int], k: int) -> [int]:
#         freq = {}
#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1
#         res = [(freq[key], key) for key in freq]
#         res.sort(reverse=True)
#         res = res[:k]
#         return [r[1] for r in res]


# #leetcode, fastest
# from collections import defaultdict
# import heapq
# class Solution:
#     def topKFrequent(self, nums: [int], k: int) -> [int]:
#         d = defaultdict(int)
#         for num in nums:
#             d[num] += 1
        
#         h = []
#         # Key = number, val is the count
#         for key, val in d.items():
#             if not h or len(h) < k: 
#                 heapq.heappush(h, (val, key))
#             else:
#                 if h[0][0] < val:
#                     heapq.heappop(h)
#                     heapq.heappush(h, (val, key))
                    
        
#         out = []
#         for _ in range(k):
#             curr = heapq.heappop(h)
#             out.append(curr[1])
#         return out


#leetcode fastest my try
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        count = Counter(nums)
        l = []
        heapq.heapify(l)
        i = 0
        for num, count_ in count.items():
            if i < k:
                i += 1
                heapq.heappush(l, (count_,num))
            else:
                if l[0][0] < count_:
                    heapq.heappop(l)
                    heapq.heappush(l, (count_, num))
        # print(l)
        return [elem[1] for elem in l]


nums = [3,0,1,0]
k = 1

nums = [1,1,1,2,2,3]
k = 2
# Output: [1,2]

# nums = [1]
# k = 1
# Output: [1]

sol = Solution()
print(sol.topKFrequent(nums, k))
