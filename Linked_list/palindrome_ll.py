'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LL:
    def __init__(self):
        self.head = None
    def addAtTail(self, val):
        node = ListNode(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
    def __str__(self):
        l = []
        current = self.head
        i = 0
        while current and i<10:
            l.append(str(current.val))
            current = current.next
            i += 1 
        return '==>'.join(l)+'==>'

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current = head
        count = 0
        odd = False
        while current:
            count += 1
            current = current.next
        if count < 2:
            return True
        if count % 2 != 0:
            odd = True
        i = 1
        current = head.next
        prev = head
        while i <= count//2 - 1:
            prev.next = current.next
            current.next = head
            head = current
            i += 1
            current = prev.next
        if odd:
            current = current.next
        while current:
            if current.val != head.val:
                return False
            current = current.next
            head = head.next
        return True

ll = LL()
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# for i in range(1, 3):
#   ll.addAtTail(i)
# for i in range(2, 1, -1):
#   ll.addAtTail(i)
ll.addAtTail(1)
ll.addAtTail(2)
print(ll)
s = Solution()
print(s.isPalindrome(ll.head))
