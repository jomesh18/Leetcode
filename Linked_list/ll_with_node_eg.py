# class MyLinkedList:

#     class Node():
#         def __init__(self, val=None):
#             self.val = val
#             self.next = None
            
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head = None
        

#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if (index>=self.length() or index<0):
#             return -1
#         else:
#             i = 0
#             current = self.head
#             while i < index:
#                 current = current.next
#                 i += 1
#             return current.val

#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         node = self.Node(val)
#         if self.head:
#             node.next = self.head
#             self.head = node
#         else:
#             self.head = node

#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         node = self.Node(val)
#         if self.head:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = node
#         else:
#             self.head = node

#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index == 0:
#             self.addAtHead(val)
#         elif index == self.length():
#             self.addAtTail(val)
#         elif index > self.length() or index < 0:
#             return -1
#         else:
#             current = self.head
#             prev = current
#             i = 0
#             while i<index:
#                 i += 1
#                 prev = current
#                 current = current.next
#             node = self.Node(val)
#             node.next = current
#             prev.next = node

#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if (index<0 or index>=self.length()):
#             return -1
#         elif index == 0:
#             self.head = self.head.next
#         else:
#             i = 0
#             prev = self.head
#             current = self.head
#             while i<index:
#                 i += 1
#                 prev = current
#                 current = current.next
#             prev.next = current.next
            
#     def length(self):
#         current = self.head
#         l = 0
#         while current:
#             l += 1
#             current = current.next
#         return l

#     def __str__(self):
#      	current = self.head
#      	ret_str = ''
#      	while current:
#      		ret_str += str(current.val) + ' --> '
#      		current = current.next
#      	return ret_str

# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)

# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

# obj = MyLinkedList()
# print(obj)
# obj.addAtHead(7)
# print(obj)
# obj.addAtHead(2)
# print(obj)
# obj.addAtHead(1)
# print(obj)
# obj.addAtIndex(3, 0)
# print(obj)
# obj.deleteAtIndex(2)
# print(obj)
# obj.addAtHead(6)
# print(obj)
# obj.addAtTail(4)
# print(obj)
# obj.get(4)
# print(obj)
# obj.addAtHead(4)
# print(obj)
# obj.addAtIndex(5, 0)
# print(obj)
# obj.addAtHead(6)
# print(obj)


# LL with list practise

class MyLinkedList:
    def __init__(self):
        self.list = []

    def addAtHead(self, val):
        self.list.insert(0, val)

    def addAtTail(self, val):
        self.list.append(val)

    def get(self, index):
        if index in range(len(self.list)):
            return self.list[index]
        return -1

    def addAtIndex(self, index, val):
        if index in range(len(self.list)):
            self.list.insert(index, val)

    def deleteAtIndex(self, index):
        if index in range(len(self.list)):
            del self.list[index]

    def get_len(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)

myll = MyLinkedList()
myll.addAtHead(1)
myll.addAtTail(3)
myll.addAtIndex(1, 2)
print(myll)
print(myll.get(1))
print(myll.get_len())
myll.deleteAtIndex(0)
print(myll)
