'''
445. Add Two Numbers II
Medium

4982

255

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None
            curr = node
            while curr:
                t = curr.next
                curr.next = prev
                prev = curr
                curr = t
            return prev if prev else curr
        
        l1, l2 = reverse(l1), reverse(l2)
        c = 0
        curr = dummy = ListNode(0)
        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            t = v1+v2+c
            c, v = t//10, t%10
            curr.next = ListNode(v)
            curr = curr.next
        return reverse(dummy.next)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        while l1:
            num1 = num1*10+l1.val
            l1 = l1.next
        while l2:
            num2 = num2*10+l2.val
            l2 = l2.next
        num = num1 + num2
        dummy = curr = ListNode(0)
        num = str(num)
        for i in range(len(num)):
            curr.next = ListNode(int(num[i]))
            curr = curr.next
        return dummy.next