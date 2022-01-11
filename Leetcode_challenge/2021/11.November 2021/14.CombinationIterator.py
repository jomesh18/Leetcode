'''
1286. Iterator for Combination
Medium

702

55

Add to List

Share
Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.
 

Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
 

Constraints:

1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 104 calls will be made to next and hasNext.
It's guaranteed that all calls of the function next are valid.
Accepted
43,415
Submissions
60,962
'''
from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.allCombinations = list(combinations(characters, combinationLength))
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return "".join(self.allCombinations[self.count-1])

    def hasNext(self) -> bool:
        return self.count < len(self.allCombinations)
        
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

true = True
false = False
null = None

inp1 = ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
inp2 = [["abc", 2], [], [], [], [], [], []]
Output = [null, "ab", true, "ac", true, "bc", false]

sol = CombinationIterator(inp2[0], inp2[1])
res = [None]

for para1, para2 in zip(inp1[1:], inp2[1:]):
    if para1 == "next":
        res.append(sol.next())
    else:
        res.append(None)
print(res)
