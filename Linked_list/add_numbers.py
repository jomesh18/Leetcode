'''
  Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LL:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head
        if curr is None:
            self.head = ListNode(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = ListNode(val)

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = ListNode(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = res = ListNode()
        c = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = (val1 + val2 + c) % 10
            c = (val1 + val2 + c) // 10
            res.next = ListNode(s)
            res = res.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if c:
            res.next = ListNode(c)
        return dummy.next

l1 = [2,4,3]
l2 = [5,6,4]
l1 = [0]
l2 = [0]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# Output: [7,0,8]

ll1 = LL()
ll2 = LL()
for i in l1:
    ll1.addAtTail(i)
for i in l2:
    ll2.addAtTail(i)
print(ll1)
print(ll2)
s = Solution()
result = LL()
result.head = s.addTwoNumbers(ll1.head, ll2.head)
print(result)
# print(ll1)
# print(ll2)
