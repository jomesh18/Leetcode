'''
Replace Words

Solution
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
Example 3:

Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"
Example 4:

Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 5:

Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
Output: "it is ab that this solution is ac"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Each two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
'''

#accepted, but too long, brute force, no trie, 4000ms
# class Solution:
#     def replaceWords(self, dictionary: [str], sentence: str) -> str:
#         sentence_list = sentence.split()
#         for pos, word in enumerate(sentence_list):
#             for i in range(len(word)):
#                 prefix = word[:i]
#                 if prefix in dictionary:
#                     sentence_list[pos] = prefix
#                     break
#         # return " ".join(sentence_list)

#using trie, faster 112ms
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isEnd = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         curr = self.root
#         for c in word:
#             curr = curr.children.setdefault(c, TrieNode())
#         curr.isEnd = True

#     def search(self, prefix):
#         curr = self.root
#         for pos, c in enumerate(prefix):
#             curr = curr.children.get(c)
#             if not curr:
#                 return prefix
#             elif curr.isEnd:
#                 return prefix[:pos+1]
#         return prefix

# class Solution:
#     def replaceWords(self, dictionary: [str], sentence: str) -> str:
#         trie = Trie()
#         for word in dictionary:
#             trie.insert(word)
#         sentence_list = sentence.split()
#         for pos, word in enumerate(sentence_list):
#             sentence_list[pos] = trie.search(word)
#         return " ".join(sentence_list)

#from leetcode, fastest
from collections import defaultdict
class Solution:
    def replaceWords(self, dictionary: [str], sentence: str) -> str:
        
        roots = defaultdict(list)
        for word in sorted(dictionary, key = lambda x: len(x)):
            roots[word[0]].append(word)
        print(roots)
        def get_root(word: str)-> str:
            for root in roots[word[0]]:
                if word.startswith(root): return root
            return word
            
            
        return " ".join([get_root(word) for word in sentence.split(" ")])

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
Output = "the cat was rat by the bat"

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
Output = "a a b c"

dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output = "a a a a a a a a bbb baba a"

dictionary = ["catt","cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
Output = "the cat was rat by the bat"

# dictionary = ["ac","ab"]
# sentence = "it is abnormal that this solution is accepted"
# Output = "it is ab that this solution is ac"

sol = Solution()
res = sol.replaceWords(dictionary, sentence)
print(res)
print(res == Output)
