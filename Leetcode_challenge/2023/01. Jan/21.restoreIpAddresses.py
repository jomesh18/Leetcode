'''
93. Restore IP Addresses
Medium

4495

738

Add to List

Share
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        if n > 12: return res
        def helper(i, curr, added, rem):
            if rem == 0 and i != n: return 
            # print(i, curr, added, rem)
            if i == n:
                if rem == 0 and not curr:
                    res.append(added)
                if rem == 1 and curr and int(curr) < 256:
                    res.append(added+[curr])
                return
            if n-i > 3*rem: return
            if curr:
                if int(curr) <= 255:
                    if s[i] != '0':
                        helper(i+1, s[i], added+[curr], rem-1)
                    else: 
                        helper(i+1, '', added+[curr]+[s[i]], rem-2)
                    if int(curr+s[i]) < 256: helper(i+1, curr+s[i], added, rem)
            else:
                if s[i] != '0':
                    helper(i+1, s[i], added, rem)
                else: 
                    helper(i+1, '', added+[s[i]], rem-1)

        helper(0, '', [], 4)
        # print(res)
        return ['.'.join(l) for l in res]


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        def dfs(idx, curr, s):
            if idx > 4: return
            if idx == 4 and not s:
                res.append(curr[:-1])
                return
            for i in range(1, len(s)+1):
                if s[:i] == '0' or (s[0] != '0' and int(s[:i]) < 256):
                    dfs(idx+1, curr+s[:i]+'.', s[i:])
        dfs(0, '', s)
        return res


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        def is_valid(start, length):
            return length == 1 or (s[start] != '0' and (length < 3 or int(s[start:start+length]) < 256))
        
        for i1 in range(max(1, n-9), min(3, n-3)+1):
            if not is_valid(0, i1):
                continue
            for i2 in range(max(1, n-6-i1), min(3, n-2-i1)+1):
                if not is_valid(i1, i2):
                    continue
                for i3 in range(max(1, n-3-i1-i2), min(3, n-1-i1-i2)+1):
                    if is_valid(i1+i2, i3) and is_valid(i1+i2+i3, n-i1-i2-i3):
                        res.append(s[:i1]+'.'+s[i1:i1+i2]+'.'+s[i1+i2:i1+i2+i3]+'.'+s[i1+i2+i3:])
        return res
