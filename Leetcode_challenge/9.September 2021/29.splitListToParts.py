'''
Split Linked List in Parts

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.


Constraints:

    The number of nodes in the list is in the range [0, 1000].
    0 <= Node.val <= 1000
    1 <= k <= 50

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head, k: int):
        if not head: return [None]*k
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        num_of_nodes = count // k
        extra_nodes = count % k
        curr = head
        res = []
        for _ in range(k):
            temp = curr
            res.append(temp)
            if curr:
                for _ in range(num_of_nodes):
                    prev = curr
                    curr = curr.next
                if extra_nodes > 0:
                    prev = curr
                    curr = curr.next
                    extra_nodes -= 1
                prev.next = None
        return res

# class Solution:
#     def splitListToParts(self, root, k):
#         # Count the length of the linked list
#         curr, length = root, 0
#         while curr:
#             curr, length = curr.next, length + 1
#         # Determine the length of each chunk
#         chunk_size, longer_chunks = length // k, length % k
#         res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
#         # Split up the list
#         prev, curr = None, root
#         for index, num in enumerate(res):
#             if prev:
#                 prev.next = None
#             res[index] = curr
#             for i in range(num):
#                 prev, curr = curr, curr.next
#         return res

def build_list(arr):
    if not arr: return None
    root = ListNode(arr[0])
    curr = root
    for e in arr[1:]:
        curr.next = ListNode(e)
        curr = curr.next
    return root

def print_list(n):
    res = []
    if n:
        curr = n
        while curr:
            res.append(curr.val)
            curr = curr.next
    return res

head = [1,2,3]
k = 5
# # Output: [[1],[2],[3],[],[]]

head = [1,2,3,4,5,6,7,8,9,10]
k = 3
# # # # Output: [[1,2,3,4],[5,6,7],[8,9,10]]

head = []
k = 3
# Output: [[],[],[]]

start = build_list(head)

sol = Solution()
ans = sol.splitListToParts(start, k)
for n in ans:
    print(print_list(n))
