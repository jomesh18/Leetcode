'''
1032. Stream of Characters
Hard

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.

For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

Implement the StreamChecker class:

    StreamChecker(String[] words) Initializes the object with the strings array words.
    boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.

 

Example 1:

Input
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output
[null, false, false, false, true, false, true, false, false, false, false, false, true]

Explanation
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the wordlist
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the wordlist
streamChecker.query("g"); // return False
streamChecker.query("h"); // return False
streamChecker.query("i"); // return False
streamChecker.query("j"); // return False
streamChecker.query("k"); // return False
streamChecker.query("l"); // return True, because 'kl' is in the wordlist

 

Constraints:

    1 <= words.length <= 2000
    1 <= words[i].length <= 2000
    words[i] consists of lowercase English letters.
    letter is a lowercase English letter.
    At most 4 * 104 calls will be made to query.

Accepted
58,026
Submissions
116,539
'''
# class Trie:
#     def __init__(self):
#         self.root = {}
     
#     def add(self, word):
#         curr = self.root
#         for i in range(len(word)-1, -1, -1):
#             curr = curr.setdefault(word[i], {})
#         curr['$'] = True
    
#     def search(self, word):
#         curr = self.root
#         for i in range(len(word)-1, -1, -1):
#             curr = curr.get(word[i], None)
#             if not curr: return False
#             if curr.get('$', None): return True
#         return False
    
# class StreamChecker:

#     def __init__(self, words: [str]):
#         self.trie = Trie()
#         for word in words:
#             self.trie.add(word)
#         self.string = ""

#     def query(self, letter: str) -> bool:
#         self.string += letter
#         return self.trie.search(self.string)


#leetcode fastest
# from collections import deque
# class StreamChecker:

#     def __init__(self, words: [str]):
#         self.trie = {}
#         self.stream = deque([])

#         for word in set(words):
#             node = self.trie       
#             for ch in word[::-1]:
#                 if not ch in node:
#                     node[ch] = {}
#                 node = node[ch]
#             node['$'] = word
        
        
#     def query(self, letter: str) -> bool:
#         self.stream.appendleft(letter)
        
#         node = self.trie
#         for ch in self.stream:
#             if '$' in node:
#                 return True
#             if not ch in node:
#                 return False
#             node = node[ch]
#         return '$' in node
    


class StreamChecker:

    def __init__(self, words: [str]):
        self.trie = {}
        self.stream = []
        for word in words:
            node = self.trie
            for i in range(len(word)-1, -1, -1):
                node = node.setdefault(word[i], {})
            node["$"] = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        for i in range(len(self.stream)-1, -1, -1):
            node = node.get(self.stream[i], None)
            if not node: return False
            if node.get('$', None): return True
        return '$' in node

    
# abc -> b - c - a - $
# xyz -> z - y - x - $

# a
# xa
# yxa
# zyxa



null = None
false = False
true = True

inp1 = ["StreamChecker", "query", "query", "query", "query"]
inp2 = [[["abc", "xyz"]], ['a'], ['x'], ['y'], ['z']]
Output = [null, false, false, false, true]

inp1 = ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
inp2 = [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output = [null, false, false, false, true, false, true, false, false, false, false, false, true]


inp1 = ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"]
inp2 = [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]
Output = [null,false,false,false,false,false,true,true,true,true,true,false,false,true,true,true,true,false,false,false,true,true,true,true,true,true,false,true,true,true,false]


obj = StreamChecker(inp2[0][0])

res = [None]

for para1, para2 in zip(inp1, inp2):
	# print(para1, para2[0])
	if para1 == 'query':
		res.append(obj.query(para2[0]))

print(res)
print(Output)
print(res == Output)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)