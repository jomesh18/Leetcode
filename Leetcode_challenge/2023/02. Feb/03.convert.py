'''
6. Zigzag Conversion
Medium

5283

11103

Add to List

Share
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = [[] for _ in range(numRows)]
        res[0].append(s[0])
        for k in range(0, len(s), 2*numRows-2):
            res[0].pop()
            start = k
            end = k + 2*numRows-2
            for i in range(numRows):
                if start < len(s): res[i].append(s[start])
                else: break
                if start == end:
                    break
                elif end < len(s):
                    res[i].append(s[end])
                start += 1
                end -= 1
            # print(res)
        # print(res)
        return ''.join((''.join(i) for i in res))
        