'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

 

Constraints:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
    The length of the linked list is between [0, 10^4].

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

ll = LL()
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
for i in range(1, 6):
    ll.addAtTail(i)
print(ll)
s = Solution()
odd_even = LL()
odd_even.head = s.oddEvenList(ll.head)
print(odd_even)

#from leetcode
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = head
        even = head.next
        evenhead = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head
#from leetcode
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head
        