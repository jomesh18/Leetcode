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
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        res = []
        curr = [root]
        while curr:
            res += [str(n.val) if n else '#' for n in curr]
            curr = [n if n else None for node in curr if node for n in [node.left, node.right]]
        return '*'.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        arr = data.split('*')
        arr = [TreeNode(val) if val != '#' else None for val in arr][::-1]
        root = arr[-1]
        q = deque([arr.pop()])
        while q:
            curr = q.popleft()
            if arr: 
                left = arr.pop()
                if left:
                    curr.left = left
                    q.append(left)
            if arr: 
                right = arr.pop()
                if right:
                    curr.right = right
                    q.append(right)
        return root

#recursive
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if not node:
                vals.append('#')
            else:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())
        def doit():
            val = next(vals)
            if val == '#': return None
            curr = TreeNode(int(val))
            curr.left = doit()
            curr.right = doit()
            return curr
        return doit()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))