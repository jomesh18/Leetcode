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
class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []

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
        curr = self.root
        for c in word:
            if curr.children:
                if c not in curr.children:
                    curr.children[c] = Node(c)
            else:
                curr.children.append(Node(c))
            curr = curr.children[c]


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pass

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pass


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

end = 2
res = []
for fn, para in zip(inp1[1: end], inp2[1: end]):
    if fn == "insert":
        res.append(trie.insert(para[0]))
    elif fn == "search":
        res.append(trie.search(para[0]))
    elif fn == "startsWith":
        res.append(trie.startsWith(para[0]))
    else:
        continue

print(res)
print(Output)
print(res == Output)