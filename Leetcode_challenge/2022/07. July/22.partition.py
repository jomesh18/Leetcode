'''
86. Partition List
Medium

4152

540

Add to List

Share
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
Accepted
375,010
Submissions
756,859
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = s = ListNode(0)
        large = l = ListNode(0)
        curr = head
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next
            curr = curr.next
        large.next = None
        if not s.next: return l.next
        head = s.next
        small.next = l.next
        return head

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = s = ListNode(0)
        large = l = ListNode(0)
        curr = head
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next
            curr = curr.next
        large.next = None
        small.next = l.next
        return s.next