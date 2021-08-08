'''
Map Sum Pairs

Solution
Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
'''
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
        self.count = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keyWords = dict()

    def containsKey(self, key):
        if key in self.keyWords:
            return self.keyWords[key]
        else:
            return 0

    def insert(self, key: str, val: int) -> None:
        count = self.containsKey(key)
        # print(key, count)
        curr = self.root
        for c in key:
            curr = curr.children[c]
            curr.count += val-count
        curr.isEnd = True
        self.keyWords[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            curr = curr.children[c]
        return curr.count

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

null = None
true = True
false = False

inp1 = ["MapSum", "insert", "sum", "insert", "sum", "insert", "sum"]
inp2 = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"], ["apple", 7], ["ap"]]
Output = [null, null, 3, null, 5, None, 9]

# inp1 = ["MapSum","insert","sum","insert","insert","sum"]
# inp2 = [[],["appled",2],["ap"],["apple",3],["apple",2],["a"]]
# Output = [null,null,2,null,null,4]

obj = MapSum()

res = [None]

for fn, para in zip(inp1, inp2):
    if fn == "insert":
        res.append(obj.insert(para[0], para[1]))
    elif fn == "sum":
        res.append(obj.sum(para[0]))
    else:
        continue

print(res)
print(Output)
print(res == Output)
