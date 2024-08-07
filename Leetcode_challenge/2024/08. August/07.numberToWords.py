'''
273. Integer to English Words
Hard

3227

6396

Add to List

Share
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
'''
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        d = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
        str_int = str(num)[::-1]
        ans = []
        for i in range(len(str_int)):
            pos = i % 3
            if i and not (i % 3):
                big_pos = i // 3
                if big_pos == 1:
                    ans.append('Thousand')
                elif big_pos == 2:
                    ans.append('Million')
                elif big_pos == 3:
                    ans.append("Billion")
                # if str_int[i] == '0':
                #     ans.pop()
                # else:
                ans.append(d[str_int[i]] if str_int[i] != '0' else '')
            else:
                if pos == 0:
                    if str_int[i] == '0':
                        ans.append('')
                    else:
                        ans.append(d[str_int[i]])
                elif pos == 1:
                    curr = str_int[i]
                    prev = str_int[i-1]
                    if curr == '0':
                        ans.append('')
                    elif curr == '1':
                        ans.pop()
                        if prev == '1':
                            ans.append('Eleven')
                        elif prev == '2':
                            ans.append('Twelve')
                        elif prev == '3':
                            ans.append('Thirteen')
                        elif prev == '4':
                            ans.append('Fourteen')
                        elif prev == '5':
                            ans.append('Fifteen')
                        elif prev == '6':
                            ans.append('Sixteen')
                        elif prev == '7':
                            ans.append('Seventeen')
                        elif prev == '8':
                            ans.append('Eighteen')
                        elif prev == '9':
                            ans.append('Nineteen')
                        elif prev == '0':
                            ans.append('Ten')
                    elif curr == '2':
                        ans.append('Twenty')
                    elif curr == '3':
                        ans.append('Thirty')
                    elif curr == '4':
                        ans.append('Forty')
                    elif curr == '5':
                        ans.append('Fifty')
                    elif curr == '6':
                        ans.append('Sixty')
                    elif curr == '7':
                        ans.append('Seventy')
                    elif curr == '8':
                        ans.append('Eighty')
                    elif curr == '9':
                        ans.append('Ninety')
                elif pos == 2:
                    if str_int[i] == '0':
                        ans.append('')
                    else:
                        ans.append(d[str_int[i]]+ ' Hundred')
        ans = ans[::-1]
        res = []
        for s in ans:
            if s:
                if s == 'Million' and res and res[-1] == 'Billion':
                    continue
                if s == 'Thousand' and res and (res[-1] == 'Million' or res[-1] == 'Billion'):
                    continue
                res.append(s)
        return ' '.join(res)
