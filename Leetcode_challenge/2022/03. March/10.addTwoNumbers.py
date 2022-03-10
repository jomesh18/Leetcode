'''

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            s = l1.val + l2.val + carry
            curr.next = ListNode(s%10)
            curr = curr.next
            carry = s // 10
            l1 = l1.next
            l2 = l2.next
        balance = l1 or l2
        while balance:
            s = balance.val + carry
            curr.next = ListNode(s%10)
            curr = curr.next
            carry = s // 10
            balance = balance.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
