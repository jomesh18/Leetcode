'''
N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

 

Constraints:

    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 104]

'''

# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> [[int]]:
        if not root: return []
        res = []
        q = deque([root])
        while q:
            l = len(q)
            level = []
            for _ in range(l):
                curr = q.popleft()
                level.append(curr.val)
                if curr.children:
                    q.extend(curr.children)
            res.append(level)
        return res

def build_nary_tree(root):
    if not root: return []
    start = Node(root[0])
    i = 2
    q = deque([start])
    while i < len(root):
        curr = q.popleft()
        child_list = []
        while i<len(root) and root[i] is not None:
            child_list.append(Node(root[i]))
            i += 1
        curr.children = child_list
        q.extend(curr.children)
        i += 1
    return start

def print_nary(start):
    if not start: return []
    q = deque([start])
    res = [start.val, None]
    while any(q):
        curr = q.popleft()
        if curr and curr.children:
            res.extend([n.val for n in curr.children])
            q.extend(curr.children)
        res.append(None)
    return res


null = None

root = [1,null,3,2,4,null,5,6]
Output = [[1],[3,2,4],[5,6]]

root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output = [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

start = build_nary_tree(root)
print(print_nary(start))

sol = Solution()
ser = sol.levelOrder(start)
print(ser)
print(ser == Output)
