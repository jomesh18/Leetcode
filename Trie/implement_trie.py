'''
Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

 

Constraints:

    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.

'''
from collections import deque
class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not self.search(word):
            curr = self.root
            for c in word:
                if c not in [n.val for n in curr.children]:
                    curr.children.append(Node(c))
                for n in curr.children:
                    if n.val == c:
                        curr = n
                        break
            curr.end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            c_in = False
            for n in curr.children:
                if c == n.val:
                    curr = n
                    c_in = True
                    break
            if not c_in:
                return False
        return True if curr.end else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            c_in = False
            for n in curr.children:
                if c == n.val:
                    curr = n
                    c_in = True
                    break
            if not c_in:
                return False
        return True

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

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

null = None
true = True
false = False

trie = Trie()

inp1 = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
inp2 = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output = [null, null, true, false, true, null, true]

# inp1 = ["Trie","insert","search","search","startsWith","insert","search"]
# inp2 = [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
# Output = [null,null,true,false,true,null,true]

end = len(inp1)
res = [None]
for fn, para in zip(inp1[1: end], inp2[1: end]):
    if fn == "insert":
        res.append(trie.insert(para[0]))
    elif fn == "search":
        res.append(trie.search(para[0]))
    elif fn == "startsWith":
        res.append(trie.startsWith(para[0]))
    else:
        continue

print(print_tree(trie.root))
print(res)
print(Output)
print(res == Output)
