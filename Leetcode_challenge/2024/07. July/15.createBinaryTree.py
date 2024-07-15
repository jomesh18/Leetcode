'''
2196. Create Binary Tree From Descriptions
Medium

1186

23

Add to List

Share
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
 

Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents = set()
        d = {}
        for p, c, l in descriptions:
            if p not in d:
                d[p] = TreeNode(p)
            if c not in d:
                d[c] = TreeNode(c)
            if l:
                d[p].left = d[c]
            else:
                d[p].right = d[c]
            parents.add(p)
            if c in parents: parents.remove(c)
        if len(parents) == 1:
            return d[parents.pop()]
        for _, c, _ in descriptions:
            if c in parents:
                parents.remove(c)
                if len(parents) == 1:
                    return d[parents.pop()]