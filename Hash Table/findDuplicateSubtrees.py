'''
Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:

Input: root = [2,1,1]
Output: [[1]]

Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

 

Constraints:

    The number of the nodes in the tree will be in the range [1, 10^4]
    -200 <= Node.val <= 200

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#tle
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tree_dict = {}
        ans = set()
        def helper(node):
            if not node: return "None"
            right = helper(node.right)
            left = helper(node.left)
            res = left+ " " +str(node.val)+" "+right
            if res in tree_dict: ans.add(tree_dict[res])
            else: tree_dict[res] = node
            return res

        helper(root)
        print(tree_dict)
        return list(ans)

#from stefan pochman O(n**2)
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tree_dict = defaultdict(list)
        def tuplify(root):
            if not root: return
            tuples = root.val, tuplify(root.left), tuplify(root.right)
            tree_dict[tuples].append(root)
            return tuples
        tuplify(root)
        return [roots[0] for roots in tree_dict.values() if len(roots) > 1]

#from stefan pochman O(n)
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def getid(root):
            if root:
                id = treeid[root.val, getid(root.left), getid(root.right)]
                trees[id].append(root)
                return id
        trees = collections.defaultdict(list)
        treeid = collections.defaultdict()
        treeid.default_factory = treeid.__len__
        # getid(root)
        # print(trees)
        # print(treeid)
        return [roots[0] for roots in trees.values() if roots[1:]]


sol = Solution()
print(sol.findDuplicateSubtrees(root))
