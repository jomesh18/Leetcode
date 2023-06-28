'''
373. Find K Pairs with Smallest Sums
Medium

5476

325

Add to List

Share
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 104
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        last_sum = float('inf')
        break_first = False
        for i in range(len(nums1)):
            if break_first:
                break
            for j in range(len(nums2)):
                s = nums1[i] + nums2[j]
                if len(heap) < k:
                    heappush(heap, (-s, i, j))
                    last_sum = -heap[0][0]
                else:
                    if s > last_sum:
                        if j == 0:
                            break_first = True
                        break
                    else: # s < -heap[0]
                        heappushpop(heap, (-s, i, j))
                        last_sum = -heap[0][0]
                        
        return [[nums1[i], nums2[j]] for _, i, j in heap]

'''
Several solutions from naive to more elaborate. I found it helpful to visualize the input as an m×n matrix of sums, for example for nums1=[1,7,11], and nums2=[2,4,6]:

      2   4   6
   +------------
 1 |  3   5   7
 7 |  9  11  13
11 | 13  15  17


Solution 5: More efficient (accepted in 104 ms)
The previous solution right away considered (the first pair of) all matrix rows (see visualization above). This one doesn't. It starts off only with the very first pair at the top-left corner of the matrix, and expands from there as needed. Whenever a pair is chosen into the output result, the next pair in the row gets added to the priority queue of current options. Also, if the chosen pair is the first one in its row, then the first pair in the next row is added to the queue.

Here's a visualization of a possible state:

# # # # # ? . .
# # # ? . . . .
# ? . . . . . .   "#" means pair already in the output
# ? . . . . . .   "?" means pair currently in the queue
# ? . . . . . .
? . . . . . . .
. . . . . . . .
As I mentioned in the comments, that could be further improved. Two of those ? don't actually need to be in the queue yet. I'll leave that as an exercise for the reader :-)
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(heap, (nums1[i]+nums2[j], i, j))
                
        ans = []
        push(0, 0)
        while heap and len(ans) < k:
            _, i, j = heappop(heap)
            ans.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        return ans