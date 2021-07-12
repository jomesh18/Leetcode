'''
Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Returns the element representing the kth largest element in the stream.

 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

 

Constraints:

    1 <= k <= 10**4
    0 <= nums.length <= 10**4
    -10**4 <= nums[i] <= 10**4
    -10**4 <= val <= 10**4
    At most 10**4 calls will be made to add.
    It is guaranteed that there will be at least k elements in the array when you search for the kth element.

'''
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None, count=1):
        self.val = val
        self.left = left
        self.right = right
        self.count = count

class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.root = None
        self.k = k
        for num in nums:
            self.root = self.add_node(self.root, num)
            print(print_tree(self.root))

    def add(self, val: int) -> int:
        self.add_node(self.root, val)
        return self.kth_largest(self.root, self.k)   
    
    def add_node(self, root, val):
        if not root:
            return TreeNode(val=val, count=1)
        if val<=root.val:
            root.left = self.add_node(root.left, val)
            root.count += 1
        elif val>root.val:
            root.right = self.add_node(root.right, val)
            root.count += 1
        return root

    def kth_largest(self, root, k):
        curr = root

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def print_tree(start):
    res = []
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append((curr.val, curr.count))
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None

inp1 = ["KthLargest", "add", "add", "add", "add", "add"]
inp2 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output = [null, 4, 5, 5, 8, 8]

obj = KthLargest(inp2[0][0], inp2[0][1])
res = [None]

for fn, para in zip(inp1, inp2):
    if fn == "add":
        res.append(obj.add(para[0]))
    else:
        pass
print(res == Output)
