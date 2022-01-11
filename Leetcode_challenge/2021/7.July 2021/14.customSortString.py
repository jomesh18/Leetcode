'''
Custom Sort String

order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

 

Note:

    order has length at most 26, and no character is repeated in order.
    str has length at most 200.
    order and str consist of lowercase letters only.

'''

class Solution(object):
    def customSortString(self, order, str):
        """
        :type order: str
        :type str: str
        :rtype: str
        """
        s = []
        dic = {}
        for c in str:
            dic[c] = dic.get(c, 0) + 1
        print(dic)
        for c in order:
            if c in dic:
                s.append(c*dic[c])
        for c in str:
            if c not in order:
                s.append(c)
        return "".join(s)

order = "cba"
str = "abcd"
# Output: "cbad"

obj = Solution()
print(obj.customSortString(order, str))
