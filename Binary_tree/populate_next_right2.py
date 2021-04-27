'''
Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

 

Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

 

Constraints:

    The number of nodes in the given tree is less than 6000.
    -100 <= node.val <= 100

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         level = [root]
#         while any(level):
#             curr = level[0]
#             for i in range(1, len(level)):
#                 curr.next = level[i]
#                 curr = curr.next
#             new_level = [elem for n in level if n for elem in (n.left, n.right) if elem]
#             level = new_level
#         return root

#from leetcode, iterative
class Solution:
    def connect(self, node):
        tail = dummy = Node(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next

def build_tree(root):
    if not root: return root
    start = Node(root[0])
    q = [start]
    i = 1
    while i<len(root):
        curr = q.pop(0)
        if curr:
            curr.left = Node(root[i]) if root[i] else None
            q.append(curr.left)
            i += 1
            curr.right = Node(root[i]) if root[i] else None
            q.append(curr.right)
            i += 1
        else:
            i += 1
    return start

def print_tree(start):
    q = [start]
    res = []
    while any(q):
        curr = q.pop(0)
        res.append(curr.val) if curr else None
        q.append(curr.left) if curr else None
        q.append(curr.right) if curr else None
    return res


root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
start = build_tree(root)
print(print_tree(start))
s = Solution()
ans = s.connect(start)
print(print_tree(ans))
