'''
211. Design Add and Search Words Data Structure
Medium

4149

168

Add to List

Share
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
Accepted
357,373
Submissions
823,042
'''

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            curr = curr.setdefault(c, {})
        curr['#'] = None

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.trie)
    
    def dfs(self, i, word, curr):
        if not curr: return False
        if i == len(word):
            if '#' in curr: return True
            else: return False
        ans = False
        if word[i] != '.':
            curr = curr.get(word[i], None)
            if not curr: return False
            ans = self.dfs(i+1, word, curr)
        else:
            for key in curr:
                ans = ans or self.dfs(i+1, word, curr[key])
                if ans: break
        return ans

null = None
true = True
false = False

obj = WordDictionary()


inp1 = ["WordDictionary","addWord","addWord","search","search","search","search","search","search","search","search"]
inp2 = [[],["a"],["ab"],["a"],["a."],["ab"],[".a"],[".b"],["ab."],["."],[".."]]
Output = [null,null,null,true,true,true,false,true,false,true,true]

inp1 = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
inp2 = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output = [null,null,null,null,false,true,true,true]

inp1 = ["WordDictionary","addWord","addWord","search","search","search"]
inp2 = [[],["bad"],["bid"],["b.c"],["baa"],[".ad"]]
Output = [None, None, None, False, False, True]

inp1 = ["WordDictionary","addWord","addWord","addWord","addWord","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search","search"]
inp2 = [[],["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"],["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]]
print(len(inp1))
Output = None

# inp1 = ["WordDictionary","addWord","addWord","search","search","search", "search"]
# inp2 = [[],["bad"],["bid"],["b.c"],["baa"],[".ad"], ["badd"]]
# Output = [None, None, None, False, False, True, False]

res = [None]

for para1, para2 in zip(inp1, inp2):
    if para1 == 'addWord':
        res.append(obj.addWord(para2[0]))
    elif para1 == 'search':
        res.append(obj.search(para2[0]))
    print(len(res), res)

print(Output)
print(res)
print(res == Output)