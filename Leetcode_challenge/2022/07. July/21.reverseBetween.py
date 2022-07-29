'''
92. Reverse Linked List II
Medium

7577

330

Add to List

Share
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
Accepted
552,934
Submissions
1,225,179
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        curr = head
        dummy = ListNode(0, head)
        last = dummy
        i = 1
        while i < left:
            last = curr
            curr = curr.next
            i += 1
        end = curr
        prev = curr
        curr = curr.next
        while i != right:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            i += 1
        last.next = prev
        end.next = curr
        return dummy.next