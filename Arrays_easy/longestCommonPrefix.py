class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs))
        res = ""
        temp = ""
        common = True
        j = 0
        while j < min_len:
            for i in range(len(strs)):
                if i == 0:
                    temp = strs[i][j]
                else:
                    if strs[i][j] != temp:
                        commom = False
                        break
            if common:
                res += temp
                j += 1
            else:
                return res

a = Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs))
