'''
328. Odd Even Linked List
Medium

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

 

Constraints:

    n == number of nodes in the linked list
    0 <= n <= 104
    -106 <= Node.val <= 106

Accepted
456,408
Submissions
778,132
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        curr = head
        even_head = ListNode()
        even_head.next = curr.next
        even = ListNode()
        last_odd = curr
        while curr and curr.next:
            even.next = curr.next
            curr.next = curr.next.next
            even = even.next
            last_odd = curr
            curr = curr.next
        if curr: curr.next = even_head.next
        else: last_odd.next = even_head.next
        even.next = None
        return head

#from leetcode
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = head
        even = head.next
        while even is not None and even.next is not None:
            temp = even.next
            even.next = temp.next
            temp.next = odd.next
            odd.next = temp
            odd = odd.next
            even = even.next
        return head