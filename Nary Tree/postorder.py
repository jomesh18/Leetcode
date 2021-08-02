'''
N-ary Tree Postorder Traversal

Solution
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

#recursive
# class Solution:
#     def postorder(self, root: 'Node') -> [int]:
#         if not root: return []
#         res = []
#         if root.children:
#             for n in root.children:
#                 res += self.postorder(n)
#         res.append(root.val)
#         return res

#iterative, reverse preorder
# class Solution:
#     def postorder(self, root: 'Node') -> [int]:
#         if not root: return []
#         res = []
#         stack = [root]
#         while stack:
#             curr = stack.pop()
#             res.append(curr.val)
#             if curr.children:
#                 stack.extend(curr.children)
#         return res[::-1]  

# iterative with visited flag
# class Solution:
#     def postorder(self, root: 'Node') -> [int]:
#         if not root: return []
#         res = []
#         stack = [(root, False)]
#         while stack:
#             curr, visited = stack.pop()
#             if visited or not curr.children:
#                 res.append(curr.val)
#             else:
#                 stack.append((curr, True))
#                 for n in curr.children[::-1]:
#                     stack.append((n, False))
#         return res

# iterative with two stacks, same logic as recursive, from leetcode
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
                        
        stack, counters, retList = [root], [0], []
        
        while len(stack) != 0:
        #To English: while the current top of the stack has an unseen child
            while counters[-1] < len(stack[-1].children):
        # Add that child to the top of the stack, with a new corresponding counter to the other stack
                stack.append(stack[-1].children[counters[-1]])
                counters.append(0)
        # If the current top of the stack has reached the end of its children list, then we pop it, it's done
            retList.append(stack.pop().val)
        # need to pop its counter as well
            counters.pop()
        # and increment the counter of the next top of the stack to begin that search
            if len(counters) != 0:
                counters[-1] += 1
            
        return retList

def build_tree(root):
    if not root: return []
    start = Node(root[0])
    i = 2
    q = deque([start])
    while i < len(root):
        curr = q.popleft()
        child_list = []
        while i<len(root) and root[i] is not None:
            child = Node(root[i])
            i += 1
            q.append(child)
            child_list.append(child)
        curr.children = child_list
        i += 1
    return start

def print_tree(start):
    if not start: return []
    res = [start.val, None]
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            if curr.children:
                q.extend(curr.children)
                res.extend([node.val for node in curr.children])
            res.append(None)
    return res

null = None

root = [1,null,3,2,4,null,5,6]
Output = [5,6,3,2,4,1]

# root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output = [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

# root = []
# Output = []

start = build_tree(root)
print(print_tree(start))

sol = Solution()
res = sol.postorder(start)
print(res)
print(res == Output)
