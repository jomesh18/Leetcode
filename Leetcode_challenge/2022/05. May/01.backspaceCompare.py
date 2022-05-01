'''
844. Backspace String Compare
Easy

4081

192

Add to List

Share
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sa = []
        ta = []
        for i, c in enumerate(s):
            if c == "#":
                if sa:
                    sa.pop()
            else:
                sa.append(c)
        for i, c in enumerate(t):
            if c == "#":
                if ta:
                    ta.pop()
            else:
                ta.append(c)      
        return sa == ta

#O(1) space
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = s.lstrip("#")
        t = t.lstrip("#")
        i, j = len(s)-1, len(t)-1
        def get_ind(k, s):
            skip = 0
            for i in range(k, -1, -1):
                if s[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    return i
            return -1
            
        while i>=0 and j>=0:
            i = get_ind(i, s)
            j = get_ind(j, t)
            print(i, j)
            if i < 0 and j < 0: return True
            if i < 0 or j < 0 or s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        if not i or not j: return False
        return True

#O(1) space
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        
        skips, skipt = 0, 0
        
        while True:
            while i>=0 and (skips or s[i] == "#"):
                skips += 1 if s[i] == "#" else -1
                i -= 1
            while j>=0 and (skipt or t[j] == "#"):
                skipt += 1 if t[j] == "#" else -1
                j -= 1
                
            if not (i>=0 and j>=0 and s[i] == t[j]):
                return i == j == -1
            i -= 1
            j -= 1