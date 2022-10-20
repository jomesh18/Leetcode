'''
12. Integer to Roman
Medium

4338

4600

Add to List

Share
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_rom = {1000: 'M', 500: "D", 100: "C", 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        ans = []
        for int_val in sorted(int_to_rom.keys(), reverse=True):
            if 900 <= num < 1000:
                ans.append('CM')
                num -= 900
            elif 400 <= num < 500:
                ans.append('CD')
                num -= 400
            elif 90 <= num < 100:
                ans.append('XC')
                num -= 90
            elif 40 <= num < 50:
                ans.append('XL')
                num -= 40
            elif num == 9:
                ans.append('IX')
                num -= 9
            elif num == 4:
                ans.append('IV')
                num -= 4
            else:
                q, r = divmod(num, int_val)
                if q:
                    ans.append(q*int_to_rom[int_val])
                    num = r
                if not num: break
        return ''.join(ans)