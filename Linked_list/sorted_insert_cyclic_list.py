'''

Sorted insert for circular linked list
Easy Accuracy: 26.7% Submissions: 33222 Points: 2

Given a sorted circular linked list, the task is to insert a new node in this circular list so that it remains a sorted circular linked list.

Example 1:

Input:
LinkedList = 1->2->4
(the first and last node is connected,
i.e. 4 --> 1)
data = 2
Output: 1 2 2 4

Example 2:

Input:
LinkedList = 1->4->7->9
(the first and last node is connected,
i.e. 9 --> 1)
data = 5
Output: 1 4 5 7 9

Your Task:
The task is to complete the function sortedInsert() which should insert the new node into the given circular linked list and return the head of the linkedlist.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
0 <= N <= 105
'''
#from geeksforgeeks
def sortedInsert(head, data):
    '''
    head:  head of given sorted circular linked list
    data:  data to be inserted
    
    return: head of resultant circular linked list
    '''
    curr = head
    n = Node(data)
    if not head:
        head = n
        head.next = n
    elif data <= head.data:
        while curr.next != head:
            curr = curr.next
        curr.next = n
        n.next = head
        head = n
    else:
        while data > curr.next.data and curr.next != head:
            curr = curr.next
        temp = curr.next
        curr.next = n
        n = temp
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def push(self, data):
        if not self.head:
            nn = Node(data)
            self.head = nn
            self.last = nn
            nn.next = nn
            return
        nn = Node(data)
        nn.next = self.head
        self.last.next = nn
        self.last = nn
def printList(head):
    if not head:
        return
    temp = head
    print(temp.data, end = ' ')
    temp = temp.next
    while temp != head:
        print(temp.data, end=' ')
        temp = temp.next

# if __name__ == '__main__':
#     t = int(input())
#     for tcs in range(t):
#         n = int(input())
#         arr = [int(x) for x in input().split()]
#         data = int(input())

#         cll = LinkedList()
#         for e in arr:
#             cll.push(e)

#         reshead = sortedInsert(cll.head, data)
#         printList(reshead)
#         print()

cll = LinkedList()
l = [1, 2, 4]
data = 2
# Output: 1 2 2 4
for e in l:
    cll.push(e)
printList(cll.head)
res = LinkedList()
res.head = sortedInsert(cll.head, data)
printList(res.head)
print('\nFinished')
