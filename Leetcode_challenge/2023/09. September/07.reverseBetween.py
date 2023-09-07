'''
92. Reverse Linked List II
Medium

10043

453

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
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        count = 0
        curr = head
        while curr and count+1 < left:
            count += 1
            prev = curr
            curr = curr.next
        while count < right and curr:
            curr = curr.next
            count += 1
        last = curr
        nex = curr
        curr = prev.next
        while curr != last:
            temp = curr.next
            curr.next = nex
            nex = curr
            curr = temp
        prev.next = nex
        return dummy.next

# One pass
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        count = 0
        curr = head
        while curr and count+1 < left:
            count += 1
            prev = curr
            curr = curr.next
        first_half_last = prev
        first = curr
        prev = curr
        curr = curr.next
        while count < right-1 and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        first_half_last.next = prev
        first.next = curr
        return dummy.next