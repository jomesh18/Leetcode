'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

    MyLinkedList() Initializes the MyLinkedList object.
    int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

 

Constraints:

    0 <= index, val <= 1000
    Please do not use the built-in LinkedList library.
    At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.


'''

# class MyLinkedList:
#     class Node:
#         def __init__(self, val=None, next=None, prev=None):
#             self.val = val
#             self.next = next
#             self.prev = prev

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head = None
#         self.tail = None

#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         current = self.head
#         count = 0
#         while current and count < index:
#             current = current.next
#             count += 1
#         if index<0 or not current:
#             return -1   
#         return current.val

#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         node = self.Node(val)
#         if self.head:
#             current = self.head
#             node.next = self.head
#             self.head.prev = node
#             self.head = node
#         else:
#             self.head = node
#             self.tail = node
#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         node = self.Node(val)
#         current = self.head
#         if current:
#             while current.next:
#                 current = current.next
#             current.next = node
#             node.prev = current
#             self.tail = node
#         else:
#             self.head = node
#             self.tail = node

#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index == 0:
#             self.addAtHead(val)
#         elif index == len(self):
#             self.addAtTail(val)
#         else:
#             node = self.Node(val)
#             current = self.head.next
#             i = 1
#             while current and i<index:
#                 current = current.next
#                 i += 1
#             node.next = current
#             node.prev = current.prev
#             current.prev.next = node
#             current.prev = node

#     def __len__(self):
#         l = 0
#         current = self.head
#         while current:
#             current = current.next
#             l += 1
#         return l

#     def __str__(self):
#         l = []
#         current = self.head
#         i = 0
#         while current and i<10:
#             l.append(str(current.val))
#             current = current.next
#             i += 1 
#         return 'Original ll: '+'==>'.join(l)+'==>'
#     def rev_print(self):
#         l = []
#         current = self.tail
#         i = 0
#         while current and i<10:
#             l.append(str(current.val))
#             current = current.prev
#             i += 1
#         return 'Reverse ll: <=='+'<=='.join(l[::-1])

#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         current = self.head
#         size = len(self)
#         if index<0 or index>=size:
#             return
#         elif index == 0 and current:
#             self.head = current.next
#             if current.next:
#                 current.next.prev = None
#             else:
#                 self.tail = self.head
#         elif index == size-1:
#             while current.next:
#                 current = current.next
#             self.tail = current.prev
#             current.prev.next = None
#         else:
#             i = 0
#             while current.next and i<index:
#                 current = current.next
#                 i += 1
#             current.prev.next = current.next
#             current.next.prev = current.prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

# obj = MyLinkedList()
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(7)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(2)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(1)
# print(obj)
# print(obj.rev_print())
# obj.addAtIndex(3, 0)
# print(obj)
# print(obj.rev_print())
# obj.deleteAtIndex(2)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(6)
# print(obj)
# print(obj.rev_print())
# obj.addAtTail(4)
# print(obj)
# print(obj.rev_print())
# print(obj.get(4))
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(4)
# print(obj)
# print(obj.rev_print())
# obj.addAtIndex(5, 0)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(6)
# print(obj)
# print(obj.rev_print())

# obj = MyLinkedList()
# obj.addAtHead(1)
# print(obj)
# print(obj.rev_print())
# obj.deleteAtIndex(0)
# print(obj)
# print(obj.rev_print())

# obj = MyLinkedList()
# obj.addAtTail(1)
# print(obj)
# print(obj.rev_print())
# print(obj.get(0))
# print(obj)
# print(obj.rev_print())

# ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
# [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

# obj = MyLinkedList()
# obj.addAtHead(2)
# print(obj)
# print(obj.rev_print())
# obj.deleteAtIndex(1)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(2)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(7)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(3)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(2)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(5)
# print(obj)
# print(obj.rev_print())
# obj.addAtTail(5)
# print(obj)
# print(obj.rev_print())
# print(obj.get(5))
# obj.deleteAtIndex(6)
# print(obj)
# print(obj.rev_print())
# obj.deleteAtIndex(6)
# print(obj)
# print(obj.rev_print())

#USING LEETCODE MY-TRY
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None

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

# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

obj = MyLinkedList()
print(obj)
print(obj.rev_print())
obj.addAtHead(7)
print(obj)
print(obj.rev_print())
obj.addAtHead(2)
print(obj)
print(obj.rev_print())
obj.addAtHead(1)
print(obj)
print(obj.rev_print())
obj.addAtIndex(3, 0)
print(obj)
print(obj.rev_print())
obj.deleteAtIndex(2)
print(obj)
print(obj.rev_print())
obj.addAtHead(6)
print(obj)
print(obj.rev_print())
obj.addAtTail(4)
print(obj)
print(obj.rev_print())
print(obj.get(4))
print(obj)
print(obj.rev_print())
obj.addAtHead(4)
print(obj)
print(obj.rev_print())
obj.addAtIndex(5, 0)
print(obj)
print(obj.rev_print())
obj.addAtHead(6)
print(obj)
print(obj.rev_print())

# obj = MyLinkedList()
# obj.addAtHead(1)
# print(obj)
# print(obj.rev_print())
# obj.deleteAtIndex(0)
# print(obj)
# print(obj.rev_print())

# obj = MyLinkedList()
# obj.addAtTail(1)
# print(obj)
# print(obj.rev_print())
# print(obj.get(0))
# print(obj)
# print(obj.rev_print())

# ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
# [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

# obj = MyLinkedList()
# obj.addAtHead(2)
# print(obj)
# print(obj.rev_print())
# obj.deleteAtIndex(1)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(2)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(7)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(3)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(2)
# print(obj)
# print(obj.rev_print())
# obj.addAtHead(5)
# print(obj)
# print(obj.rev_print())
# obj.addAtTail(5)
# print(obj)
# print(obj.rev_print())
# print(obj.get(5))
# obj.deleteAtIndex(6)
# print(obj)
# print(obj.rev_print())
# obj.deleteAtIndex(6)
# print(obj)
# print(obj.rev_print())