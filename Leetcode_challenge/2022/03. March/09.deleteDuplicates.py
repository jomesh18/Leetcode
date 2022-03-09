'''
82. Remove Duplicates from Sorted List II
Medium

5049

159

Add to List

Share
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
Accepted
447,627
Submissions
1,033,386
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            if not stack:
                stack.append(curr)
                curr = curr.next
            else:
                if stack[-1].val == curr.val:
                    value = stack[-1].val
                    stack.pop()
                    while curr and curr.val == value:
                        curr = curr.next
                else:
                    stack.append(curr)
                    curr = curr.next
        dummy = ListNode()
        curr = dummy
        for node in stack:
            curr.next = node
            curr = curr.next
        curr.next = None
        return dummy.next

#O(n), O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        pred = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return dummy.next
