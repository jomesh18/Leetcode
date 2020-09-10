class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        min_len = len(strs[0])
        for i in strs:
            if min_len>len(i):
                min_len = len(i)
        res = ""
        temp = ""
        common = True
        j = 0
        while j < min_len:
            for i in range(len(strs)):
                print(i, j)
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
