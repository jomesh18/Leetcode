'''
117. Populating Next Right Pointers in Each Node II
Medium

3946

243

Add to List

Share
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
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
#O(n) time, space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        level = [root]
        while level:
            next_lev = [n for node in level for n in [node.left, node.right] if n]
            for i in range(len(next_lev)-1):
                next_lev[i].next = next_lev[i+1]
            level = next_lev[:]
        return root

#O(n) time, O(1) space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        curr = root
        prev = None
        next_lev = None
        while curr:
            while curr:
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        next_lev = curr.left
                    prev = curr.left
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        next_lev = curr.right
                    prev = curr.right
                curr = curr.next
            curr = next_lev
            prev = None
            next_lev = None
        return root

#O(n) time, O(1) space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(0)
        n_level = dummy
        node = root
        while node:
            n_level.next = node.left
            if n_level.next: n_level = n_level.next
            n_level.next = node.right
            if n_level.next: n_level = n_level.next
            node = node.next
            if not node:
                node = dummy.next
                # dummy.next = None
                n_level = dummy
        return root