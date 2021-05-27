'''
Serialize and Deserialize Binary Tree

Solution
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#my try
# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root: return str([])
#         q = [root]
#         res = []
#         while any(q):
#         	curr = q.pop(0)
#         	res.append(str(curr.val) if curr else "null")
#         	if curr:
#         		q.extend([curr.left, curr.right])
#         return ','.join(res)

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         if data == '[]' or data == []: return None
#         nodes = [None if val == 'null' else TreeNode(int(val)) for val in data.strip('[]').split(',')]
#        	reverse = nodes[::-1]
#        	root = reverse.pop()
#        	for node in nodes:
#        		if node:
#        			if reverse: node.left = reverse.pop()
#        			if reverse: node.right = reverse.pop()
#        	return root

#from leetcode
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

def create_tree(root):
	if not root: return root
	start = TreeNode(root[0]) if root[0] is not None else None
	i = 1
	q = [start]
	while i<len(root):
		curr = q.pop(0)
		if curr:
			if root[i] is not None:
				curr.left = TreeNode(root[i])
				q.append(curr.left)
			i += 1
			if i < len(root) and root[i] is not None:
				curr.right = TreeNode(root[i])
				q.append(curr.right)
			i += 1
	return start

def print_tree(root):
	if not root: return root
	q = [root]
	res = []
	while any(q):
		curr = q.pop(0)
		res.append(curr.val if curr else None)
		if curr: q.extend([curr.left, curr.right])
	return res


root = [1,2,3,None,None,4,5]
root = []
# Output: [1,2,3,null,null,4,5]
root = create_tree(root)
# print(print_tree(root))

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
print(ser.serialize(root))
ans = deser.deserialize(ser.serialize(root))
print(print_tree(root))