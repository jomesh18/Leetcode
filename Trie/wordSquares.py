'''
Word Squares
Description

Given a set of words without duplicates, find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l

a r e a

l e a d

l a d y

    There are at least 1 and at most 1000 words.
    All words will have the exact same length.
    Word length is at least 1 and at most 5.
    Each word contains only lowercase English alphabet a-z.

Example

Example 1:

Input:

["area","lead","wall","lady","ball"]

Output:

[["wall","area","lead","lady"],["ball","area","lead","lady"]]



Explanation:

The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Example 2:

Input:

["abat","baba","atan","atal"]

Output:

 [["baba","abat","baba","atan"],["baba","abat","baba","atal"]
 '''
# class Trie:
#     def __init__(self):
#         self.root = {}
    
#     def insert(self, word):
#         current = self.root
#         for c in word:
#             current = current.setdefault(c, {})
#         current["#"] = word

#     def search(self, prefix):
#         current = self.root
#         for c in prefix:
#             current = current.get(c)
#             if not current: return (False, [])
#         word_list = []
#         def dfs(node):
#             if "#" in node:
#                 word_list.append(node["#"])
#             for n in node:
#                 if n == "#": continue
#                 dfs(node[n])
#         dfs(current)
#         return (True, word_list)

# class Solution:
#     """
#     @param words: a set of words without duplicates
#     @return: all word squares
#     """
#     def wordSquares(self, words):
#         # write your code here
#         if not words: return []
#         m = len(words[0])
#         res = []
#         trie = Trie()
#         for word in words:
#             trie.insert(word)
#         res = []
#         def find_squares(pos, words_list):
#             # print(pos, words_list)
#             if pos == m:
#                 res.append(words_list[:])
#                 return
#             prefix = ""
#             for w in words_list:
#                 prefix += w[pos]
#             status, candidates = trie.search(prefix)
#             if status:
#                 for word in candidates:
#                     words_list.append(word)
#                     find_squares(pos+1,words_list)
#                     words_list.pop()
                
#         for word in words:
#             find_squares(1, [word])
#         return res


words = ["area","lead","wall","lady","ball"]
# # Output = [["wall","area","lead","lady"],["ball","area","lead","lady"]]

words = ["abat","baba","atan","atal"]
# # Output = [["baba","abat","baba","atan"],["baba","abat","baba","atal"]

words = []

sol = Solution()
print(sol.wordSquares(words))
