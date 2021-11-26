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
# import heapq
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: [int], k: int) -> [int]:
#         count = Counter(nums)
#         l = []
#         heapq.heapify(l)
#         i = 0
#         for num, count_ in count.items():
#             if i < k:
#                 i += 1
#                 heapq.heappush(l, (count_,num))
#             else:
#                 if l[0][0] < count_:
#                     heapq.heappop(l)
#                     heapq.heappush(l, (count_, num))
#         # print(l)
#         return [elem[1] for elem in l]

'''
Python] 5 lines O(n) buckets solution, explained.
313
DBabichev's avatar
DBabichev
24731

July 17, 2020 12:59 PM

15.3K VIEWS

There are solution, using quickselect with O(n) complexity in average, but I think they are overcomplicated: actually, there is O(n) solution, using bucket sort. The idea, is that frequency of any element can not be more than n. So, the plan is the following:

    Create list of empty lists for bucktes: for frequencies 1, 2, ..., n.
    Use Counter to count frequencies of elements in nums
    Iterate over our Counter and add elements to corresponding buckets.
    buckets is list of lists now, create one big list out of it.
    Finally, take the k last elements from this list, these elements will be top K frequent elements.

Complexity: time complexity is O(n), because we first iterate over nums once and create buckets, then we flatten list of lists with total number of elements O(n) and finally we return last k elements. Space complexity is also O(n).
'''
class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]

If you have any questions, feel free to ask. If you like solution and explanations, please Upvote!
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
