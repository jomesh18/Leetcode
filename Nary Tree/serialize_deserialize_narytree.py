'''
765. Serialize and Deserialize N-ary Tree
Difficulty: Hard

Topics: Tree

Similar Questions:

Serialize and Deserialize Binary Tree

Serialize and Deserialize BST

Encode N-ary Tree to Binary Tree

Problem:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree

 



 

as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Note:

N is in the range of  [1, 1000]
Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''


# Definition for a directed graph node
from collections import deque
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def serialize(self, root):
        if not root: return []
        q = deque([root])
        res = [root.label, None]
        while any(q):
            curr = q.popleft()
            if curr and curr.neighbors:
                res.extend([n.label for n in curr.neighbors])
                q.extend(curr.neighbors)
            res.append(None)
        return ','.join(str(i) for i in res)

    def deserialize(self, data):
        if not data: return []
        root = [int(i) if i!="None" else None for i in data.split(",")]
        start = DirectedGraphNode(root[0])
        i = 2
        q = deque([start])
        while i < len(root):
            curr = q.popleft()
            while i<len(root) and root[i] is not None:
                curr.neighbors.append(DirectedGraphNode(root[i]))
                i += 1
            q.extend(curr.neighbors)
            i += 1
        return start

def build_nary_tree(root):
    if not root: return []
    start = DirectedGraphNode(root[0])
    i = 2
    q = deque([start])
    while i < len(root):
        curr = q.popleft()
        while i<len(root) and root[i] is not None:
            curr.neighbors.append(DirectedGraphNode(root[i]))
            i += 1
        q.extend(curr.neighbors)
        i += 1
    return start

def print_nary(start):
    if not start: return []
    q = deque([start])
    res = [start.label, None]
    while any(q):
        curr = q.popleft()
        if curr and curr.neighbors:
            res.extend([n.label for n in curr.neighbors])
            q.extend(curr.neighbors)
        res.append(None)
    return res

root = [1, None, 2, 3, 4, None, 5, None, 6]

root = [1, None, 3, 2, 4, None, 5, 6]
# {1,2,3,4#2#3,5,6#4#5#6}

start = build_nary_tree(root)
print(print_nary(start))

sol = Solution()
ser = sol.serialize(start)
print(ser)
deser = sol.deserialize(ser)
print(print_nary(deser))
