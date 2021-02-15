'''
Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

 

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        current, size = head, 1
        while current.next:
            size += 1
            current = current.next
        current.next = head
        size = size - (k % size)
        current = head
        for _ in range(size-1):
            current = current.next
        head = current.next
        current.next = None
        return head

head = [1,2,3,4,5]
k = 2
# Output: [4,5,1,2,3]
head = [0,1,2]
k = 4
# Output: [2,0,1]
ll = LL()
for i in head:
    ll.addAtTail(i)
print(ll)
print(k)
s = Solution()
res_ll = LL()
res_ll.head = s.rotateRight(ll.head, k)
print(res_ll)
