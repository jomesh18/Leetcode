'''
28. Find the Index of the First Occurrence in a String
Medium

2197

123

Add to List

Share
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''
# using library function
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# rabin karp single hash
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if n < m: return -1
        radix, mod = 26, 10**9+33
        max_weight = 1
        for _ in range(m):
            max_weight = (max_weight*radix)%mod
            
        curr_hash, needle_hash = 0, 0
        for i in range(m):
            curr_hash = (curr_hash+((ord(haystack[i])-ord('a'))*(radix**(m-1-i)))%mod)%mod
            needle_hash = (needle_hash+((ord(needle[i])-ord('a'))*(radix**(m-1-i)))%mod)%mod
        if curr_hash == needle_hash and haystack[:m] == needle: return 0
        # print(curr_hash, needle_hash)
        for i in range(1, n-m+1):
            curr_hash = (curr_hash*radix)%mod
            curr_hash = ((curr_hash-((ord(haystack[i-1])-ord('a'))*max_weight))+mod)%mod
            curr_hash = (curr_hash+(ord(haystack[i+m-1])-ord('a')))%mod
            # print(i, curr_hash)
            if curr_hash == needle_hash and haystack[i:i+m] == needle: return i
        return -1

# rabin karp, multiple hash O(n+m)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if n < m: return -1
        radix1, radix2 = 26, 31
        mod1, mod2 = 10**9+33, 10**9+7
        max_w1, max_w2 = 1, 1
        for _ in range(m):
            max_w1 = (max_w1*radix1)%mod1
            max_w2 = (max_w2*radix2)%mod2
        def find_hash(word, start, end, radix, mod):
            curr_hash = 0
            factor = 1
            for i in range(end, start-1, -1):
                curr_hash = (curr_hash + ((ord(word[i])-ord('a'))*factor)%mod)%mod
                factor = (factor*radix)%mod
            return curr_hash
        nhash1, nhash2 = find_hash(needle, 0, m-1, radix1, mod1), find_hash(needle, 0, m-1, radix2, mod2)
        hhash1, hhash2 = find_hash(haystack, 0, m-1, radix1, mod1), find_hash(haystack, 0, m-1, radix2, mod2)
        if hhash1 == nhash1 and hhash2 == nhash2: return 0
        def find_rolling(curr_hash, word, length, start, radix, mod, max_w):
            curr_hash = (curr_hash*radix)%mod
            curr_hash = (curr_hash-((ord(word[start-1])-ord('a'))*max_w)+mod)%mod
            curr_hash = (curr_hash+(ord(word[start+length-1])-ord('a')))%mod
            return curr_hash
        # print(hhash1, hhash2, nhash1, nhash2)
        for i in range(1, n-m+1):
            hhash1 = find_rolling(hhash1, haystack, m, i, radix1, mod1, max_w1)
            hhash2 = find_rolling(hhash2, haystack, m, i, radix2, mod2, max_w2)
            # print(hhash1, hhash2, i)
            if (hhash1 == nhash1) and (hhash2 == nhash2): return i
        return -1