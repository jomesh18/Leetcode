class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) == 0: return ""
        min_len = len(strs[0])
        for i in strs:
            if min_len>len(i):
                min_len = len(i)
        res = []
        temp = ""
        common = True
        j = 0
        while j < min_len:
            for i in range(len(strs)):
                if i == 0:
                    temp = strs[i][j]
                else:
                    if strs[i][j] != temp:
                        common = False
                        break
            if common:
                res.append(temp)
                j += 1
            else:
                return "".join(res)
        return "".join(res)

a = Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs) =='fl')
#Edge cases
strs = [""]
print(a.longestCommonPrefix(strs)=="")
strs = []
print(a.longestCommonPrefix(strs)=="")
strs = ["", ""]
print(a.longestCommonPrefix(strs)=="")
strs = ["a"]
print(a.longestCommonPrefix(strs)=="a")
strs = ["a", "", "c"]
print(a.longestCommonPrefix(strs)=="")
strs = ["c","c"]
<<<<<<< HEAD
print(a.longestCommonPrefix(strs))

#From Leetcode
def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest
=======
print(a.longestCommonPrefix(strs)=="c")
>>>>>>> 329adadbf4a16bbbc7b91f909cece94659e673ba
