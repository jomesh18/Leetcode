'''
143. Reorder List
Medium

10541

374

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid using floyd's cycle detection algo
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # break both halves into two
        if fast:
            prev = slow
            slow = slow.next
        prev.next = None
        # reverse second half
        prev = None
        while slow:
            t = slow.next
            slow.next = prev
            prev = slow
            slow = t
        # combine both 
        curr1 = head
        curr2 = prev
        while curr1:
            t = curr1.next
            curr1.next = curr2
            if curr2:
                curr2 = curr2.next
                curr1.next.next = t
            curr1 = t
        return head