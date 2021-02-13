'''
  Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

 

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example 4:

Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.

 

Constraints:

    0 <= n <= 1000
    -10000 <= Node.val <= 10000
    Node.random is null or is pointing to some node in the linked list.


'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class LL:
    def __init__(self):
        self.head = None

    def addAtTail(self, val):
        node = Node(val)
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
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        current = head
        while current:
        	temp = current.next
        	current.next = Node(current.val)
        	current.next.next = temp
        	current = current.next.next
        current = head
        while current:
        	current.next.random = current.random if not current.random else current.random.next
        	current = current.next.next
        current = head.next
        while current.next:
        	current.next = current.next.next
        	current = current.next
        return head.next

ll = LL()
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
for i in head:
	ll.addAtTail(i[0])
print(ll)
main_loop = ll.head
for i in head:
	current = ll.head
	pos = i[1]
	if pos is None:
		main_loop.random = pos
	else:
		while pos>0:
			pos -= 1
			current = current.next
		main_loop.random = current
	main_loop = main_loop.next
l = []
head = ll.head
while head:
	l.append((head.val, head.random.val if head.random else head.random))
	head = head.next
print(l)
copy_ll = LL()
s = Solution()
copy_ll.head = s.copyRandomList(ll.head)
print(copy_ll)
head = copy_ll.head
l = []
while head:
	l.append((head.val, head.random.val if head.random else head.random))
	head = head.next
print(l)
print('finished')