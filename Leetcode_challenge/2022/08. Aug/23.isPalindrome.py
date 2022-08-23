'''
234. Palindrome Linked List
Easy

10876

630

Add to List

Share
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def rev(prev, curr):
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
            return (prev, curr)
        # print(head)
        dummy = ListNode(0, head)
        prev, fast, slow = dummy, head, head
        while fast and fast.next:
            fast = fast.next.next
            prev, slow = rev(prev, slow)
        #if ll length is even, slow will point to starting of second half, fast is None
        # if ll length is odd, slow will point to mid element, fast.next is None
        is_palin = True
        if not fast:
            backward, forward = prev, slow
            prev = slow
        elif not fast.next:
            backward, forward = prev, slow.next
            prev = slow
        while backward and forward:
            if backward.val != forward.val:
                is_palin = False
            forward = forward.next
            prev, backward = rev(prev, backward)
        backward.next = prev
        # print(head)
        return is_palin