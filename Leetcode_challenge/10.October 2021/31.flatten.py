'''
430. Flatten a Multilevel Doubly Linked List
Medium

3022

225

Add to List

Share
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 105
'''

# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        stack = [head]
        prev = Node(0, None, None, None)

        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        head.prev = None
        return head

def build_doubly_ll(head):
    if not head: return head
    root = Node(head[0], None, None, None)
    i = 1
    curr = root
    level_start = root
    while i < len(head) and head[i] != None:
        while i < len(head) and head[i] != None:
            curr.next = Node(head[i], curr, None, None)
            curr = curr.next
            i += 1
        curr = level_start
        i += 1
        while i < len(head) and head[i] == None:
            i += 1
            curr = curr.next
        if i >= len(head): break
        curr.child = Node(head[i], None, None, None)
        # print(curr.val)
        curr = curr.child
        level_start = curr
        # print(level_start.val if level_start else None)
        i += 1
    return root

#todo
# def print_doubly_ll(root):
#     res = []
#     if not root: return root
#     curr = root
#     next_level_q = deque()
#     while curr or next_level_q:
#         while curr:
#             res.append(curr.val)
#             next_level_q.append(curr.child)
#             curr = curr.next
#         curr = next_level_q.popleft()
#         while not curr and next_level_q:
#             res.append(None)
#             curr = next_level_q.popleft()
#     return res


null = None

head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]

# head = [1,2,null,3]
# # Output: [1,3,2]

# head = []
# # Output: []

root = build_doubly_ll(head)
print(print_doubly_ll(root))

sol = Solution()
print(sol.flatten(root))
