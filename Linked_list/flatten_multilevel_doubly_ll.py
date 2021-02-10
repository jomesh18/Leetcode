'''
  Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Example 3:

Input: head = []
Output: []

 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

 

Constraints:

    The number of Nodes will not exceed 1000.
    1 <= Node.val <= 105

'''

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<0 or index>=self.size:
            return -1
        if not self.head:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index<0 or index>self.size:
            return
        node = Node(val)
        if index == 0:
            if self.head:
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                self.head = node
                self.tail = node
        elif index == self.size:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0 or index>=self.size:
            return
        current = self.head
        if index == 0:
            if self.size == 0:
                return
            elif self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            for _ in range(index-1):
                current = current.next
            current.next.next.prev = current.next.prev
            current.next = current.next.next

        self.size -= 1

    def __str__(self):
        l = []
        current = self.head
        while current:
            l.append(str(current.val))
            current = current.next
        return 'Original ll: '+'==>'.join(l)+'==>'
        
    def rev_print(self):
        l = []
        current = self.tail
        while current:
            l.append(str(current.val))
            current = current.prev
        return 'Reverse ll: <=='+'<=='.join(l[::-1])
# with stack
# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         if not head:
#             return head
#         stack = [head]
#         prev = Node(0)

#         while stack:
#             curr = stack.pop()
#             prev.next = curr
#             curr.prev = prev

#             if curr.next:
#                 stack.append(curr.next)
#             if curr.child:
#                 stack.append(curr.child)
#             prev = curr
#         head.prev = None
#         return head

# without stack
'''
    Iterate list from head and create current node
    Loop until current is not null
    Check if current don't have child just update current to current.next and continute [case of simple dll]
    If child node exit then find the tail of child dll and join that tail to before the current.next
    If current.next is not null change the prev to temp [tail of current child chain]
    Update current.next to current.child and also change the prev of current.child to current and null child node [mark visited this child node]
'''
# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         curr = head
#         while curr:
#             if curr.child:
#                 c = curr.child
#                 while c.next:
#                     c = c.next
#                 if curr.next:
#                     c.next = curr.next
#                     curr.next.prev = c
#                 curr.next = curr.child
#                 curr.child.prev = curr
#                 curr.child = None
#             curr = curr.next
#         return head

# recursive from leetcode
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return (None)
        self.travel(head)
        return (head)

    def travel(self, cur):
        while cur:
            next_node = cur.next # have to store next node in case cur.next gets overridden to point to child node. will use this to connect the child level back to current level
            if not next_node: tail = cur  # reached the last node in current level, assign it to 'tail' for return

            if cur.child: # if the current node contains a child node, this if clause will handle the child node's level and any more child nodes that it spawns
                cur.child.prev = cur
                cur.next = cur.child

                child_tail = self.travel(cur.child) #returns tail after traversing the child node's level
                if next_node:     # if there exists a node in the prior level, connect its prev pointer to the child node's tail. if there is none, then no need
                    next_node.prev = child_tail

                child_tail.next = next_node  # have to connect child_tail back to prior level regardless if next node is null or not
                cur.child = None  # clearing child pointers

            cur = cur.next  # this will either begin traversing cur's child node level (if exists) or resume traversing cur's current level

        return (tail)  # returns tail node of level  

ll = MyLinkedList()
ll.addAtTail(1)
ll.addAtTail(2)
ll.addAtTail(3)
current = ll.head
current = current.next
current.child = Node(4)
current.child.next = Node(5)
current.child.next.prev = current.child
s = Solution()
flat_ll = MyLinkedList()
flat_ll.head = s.flatten(ll.head)
print(flat_ll)
print(flat_ll.rev_print())
print(ll)
print(ll.rev_print())
