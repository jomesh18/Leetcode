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
# wont work now, extensive changes in the new one
#my try
# class Node:
#     def __init__(self, val=None):
#         self.val = val
#         self.children = []
#         self.end = False

# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = Node()


#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         if not self.search(word):
#             curr = self.root
#             for c in word:
#                 if c not in [n.val for n in curr.children]:
#                     curr.children.append(Node(c))
#                 for n in curr.children:
#                     if n.val == c:
#                         curr = n
#                         break
#             curr.end = True


#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         curr = self.root
#         for c in word:
#             c_in = False
#             for n in curr.children:
#                 if c == n.val:
#                     curr = n
#                     c_in = True
#                     break
#             if not c_in:
#                 return False
#         return True if curr.end else False

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         curr = self.root
#         for c in prefix:
#             c_in = False
#             for n in curr.children:
#                 if c == n.val:
#                     curr = n
#                     c_in = True
#                     break
#             if not c_in:
#                 return False
#         return True

class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.links = [None] * 26
        self.isEnd = False

    def containsKey(self, key):
        return self.links[ord(key)-ord('a')] != None

    def get(self, key):
        return self.links[ord(key)-ord('a')]

    def put(self, key, node):
        self.links[ord(key)-ord('a')] = node

    def isEnd(self):
        return self.isEnd

    def setIsEnd(self):
        self.isEnd = True

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()  

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if not curr.containsKey(c):
                curr.put(c, TrieNode())
            curr = curr.get(c)
        curr.setIsEnd()

    def searchPrefix(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if not curr.containsKey(c):
                return False
            curr = curr.get(c)
        return curr

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.searchPrefix(word)
        return curr if not curr else curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return bool(self.searchPrefix(prefix))

#from leetcode, using dict
# class TrieNode:
#     # Initialize your data structure here.
#     def __init__(self):
#         self.word=False
#         self.children={}
    
# class Trie:
    
#     def __init__(self):
#         self.root = TrieNode()

#     # @param {string} word
#     # @return {void}
#     # Inserts a word into the trie.
#     def insert(self, word):
#         node=self.root
#         for i in word:
#             if i not in node.children:
#                 node.children[i]=TrieNode()
#             node=node.children[i]
#         node.word=True

#     # @param {string} word
#     # @return {boolean}
#     # Returns if the word is in the trie.
#     def search(self, word):
#         node=self.root
#         for i in word:
#             if i not in node.children:
#                 return False
#             node=node.children[i]
#         return node.word

#     # @param {string} prefix
#     # @return {boolean}
#     # Returns if there is any word in the trie
#     # that starts with the given prefix.
#     def startsWith(self, prefix):
#         node=self.root
#         for i in prefix:
#             if i not in node.children:
#                 return False
#             node=node.children[i]
#         return True

#from leetcode, defaultdict
# class TrieNode:
#     # Initialize your data structure here.
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.is_word = False
        
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         current = self.root
#         for letter in word:
#             current = current.children[letter]
#         current.is_word = True

#     def search(self, word):
#         current = self.root
#         for letter in word:
#             current = current.children.get(letter)
#             if current is None:
#                 return False
#         return current.is_word

#     def startsWith(self, prefix):
#         current = self.root
#         for letter in prefix:
#             current = current.children.get(letter)
#             if current is None:
#                 return False
#         return True

#recursive, not working
# def print_trie(root):


#iterative bfs, working
# def print_trie(root):
#     res = []
#     q = deque([(root, '')])
#     while q:
#         curr, word = q.popleft()
#         if curr:
#             for pos, node in enumerate(curr.links):
#                 if node:
#                     q.append((node, word+'abcdefghijklmnopqrstuvwxyz'[pos]))
#                     if node.isEnd: res.append(q[-1][-1])            
#     return res

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

null = None
true = True
false = False

trie = Trie()

# inp1 = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# inp2 = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output = [null, null, true, false, true, null, true]

# # inp1 = ["Trie","insert","search","search","startsWith","insert","search"]
# # inp2 = [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
# # Output = [null,null,true,false,true,null,true]

# res = [None]
# for fn, para in zip(inp1, inp2):
#     if fn == "insert":
#         res.append(trie.insert(para[0]))
#     elif fn == "search":
#         res.append(trie.search(para[0]))
#     elif fn == "startsWith":
#         res.append(trie.startsWith(para[0]))
#     else:
#         continue

# print(print_trie(trie.root))
# print(res)
# print(Output)
# print(res == Output)

trie.insert('ba')
trie.insert('bad')
trie.insert('ca')
print(print_trie(trie.root))

