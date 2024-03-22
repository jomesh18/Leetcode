'''
234. Palindrome Linked List
Easy

16003

864

Add to List

Share
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

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
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            t = slow.next
            slow.next = prev
            prev = slow
            slow = t
        if fast:
            rev = slow
            forward = slow.next
            ans = True
        else:
            forward = slow.next
            t = prev.next
            prev.next = slow
            rev = prev
            prev = t
            ans = True
        while forward:
            if rev.val != forward.val:
                ans = False
            t = prev.next
            prev.next = rev
            rev = prev
            prev = t
            forward = forward.next
        return ans