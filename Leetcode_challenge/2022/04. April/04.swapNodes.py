'''
1721. Swapping Nodes in a Linked List
Medium

2196

87

Add to List

Share
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
Accepted
127,037
Submissions
188,464
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        from_front, from_back = k-1, n-k
        # print(n, from_front, from_back)
        curr = head
        i = 0
        from_front_node, from_back_node = None, None
        while curr:
            if i == from_front:
                from_front_node = curr
            if i == from_back:
                from_back_node = curr
            curr = curr.next
            i += 1
            if from_front_node and from_back_node:
                from_front_node.val, from_back_node.val = from_back_node.val, from_front_node.val
                break
        return head

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1, p2 = None, None
        i = k
        p = head
        while p:
            i -= 1
            p2 = p2.next if p2 else None
            if i == 0:
                p1 = p
                p2 = head
            p = p.next
        if p2:
            p2.val, p1.val = p1.val, p2.val
        return head