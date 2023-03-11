'''
109. Convert Sorted List to Binary Search Tree
Medium

5993

132

Add to List

Share
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def build(head, limit):
            if not limit: return head
            if limit == 1: return TreeNode(head.val)
            if limit == 2: return TreeNode(head.val, None, TreeNode(head.next.val))
            mid = limit // 2
            curr = head
            for _ in range(mid):
                curr = curr.next
            root = TreeNode(curr.val)
            
            root.right = build(curr.next, limit-1-mid)
            root.left = build(head, limit-mid-(1 if limit&1 else 0))
            return root
        
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        return build(head, n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def build(head, tail):
            if head == tail: return None
            f, s = head, head
            while f != tail and f.next != tail:
                f = f.next.next
                s = s.next
            root = TreeNode(s.val)
            root.left = build(head, s)
            root.right = build(s.next, tail)
            return root
            
        return build(head, None)