'''
745. Prefix and Suffix Search
Hard

1960

453

Add to List

Share
Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
 

Constraints:

1 <= words.length <= 104
1 <= words[i].length <= 7
1 <= pref.length, suff.length <= 7
words[i], pref and suff consist of lowercase English letters only.
At most 104 calls will be made to the function f.
'''
trie = lambda: defaultdict(trie)
pos = False
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = trie()
        for p, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                curr = self.trie
                curr[pos] = i
                for j in range(i, 2*len(word)-1):
                    curr = curr[word[j%len(word)]]
                    curr[pos] = p
                    
    def f(self, pref: str, suff: str) -> int:
        curr = self.trie
        for c in suff+'#'+pref:
            if c not in curr:
                return -1
            curr = curr[c]
        return curr[pos]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)