'''
Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Returns the element representing the kth largest element in the stream.

 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

 

Constraints:

    1 <= k <= 10**4
    0 <= nums.length <= 10**4
    -10**4 <= nums[i] <= 10**4
    -10**4 <= val <= 10**4
    At most 10**4 calls will be made to add.
    It is guaranteed that there will be at least k elements in the array when you search for the kth element.

'''
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None, coun=1):
        self.val = val
        self.left = left
        self.right = right
        self.coun = coun

# time limit exceeded
# class KthLargest:
#     def __init__(self, k: int, nums: [int]):
#         self.root = None
#         self.k = k
#         for num in nums:
#             self.root = self.add_node(self.root, num)
#             print(print_tree(self.root))

#     def add(self, val: int) -> int:
#         self.root = self.add_node(self.root, val)
#         return self.kth_largest(self.root, self.k)
    
#     def add_node(self, root, val):
#         if not root:
#             return TreeNode(val=val, coun=1)
#         if val<=root.val:
#             root.left = self.add_node(root.left, val)
#             root.coun += 1
#         elif val>root.val:
#             root.right = self.add_node(root.right, val)
#             root.coun += 1
#         return root

#     def kth_largest(self, root, k):
#         curr = root
#         while curr:
#             if curr.left:
#                 diff = curr.coun-curr.left.coun
#                 if diff == k:
#                     return curr.val
#                 elif diff < k:
#                     k -= diff
#                     curr = curr.left
#                 else:
#                     curr = curr.right
#             elif curr.right:
#                 if curr.coun == k:
#                     return curr.val
#                 curr = curr.right
#             else:
#                 if curr.coun == k:
#                     return curr.val

import heapq
class KthLargest:
    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.l = []
        for num in nums:
            self.add(num)
            # print(self.l)

    def add(self, val: int) -> int:
        if len(self.l) < self.k:
            heapq.heappush(self.l, val)
        elif val > self.l[0]:
            heapq.heappop(self.l)
            heapq.heappush(self.l, val)
        return self.l[0]

#from leetcode
class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

            
    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def print_tree(start):
    res = []
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append((curr.val, curr.coun))
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None

inp1 = ["KthLargest", "add", "add", "add", "add", "add"]
inp2 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output = [null, 4, 5, 5, 8, 8]

# inp1 = ["KthLargest","add","add","add","add","add"]
# inp2 = [[1,[]],[-3],[-2],[-4],[0],[4]]
# Output = [null,-3,-2,-2,0,4]

obj = KthLargest(inp2[0][0], inp2[0][1])
res = [None]

for fn, para in zip(inp1, inp2):
    if fn == "add":
        ans = obj.add(para[0])
        print(ans)
        res.append(ans)
    else:
        pass
print(res == Output)
