'''

'''

class Solution:
    def findMaximumXOR(self, nums: [int]) -> int:
        trie = {}
        largest = max(nums)
        length = len(bin(largest))-2
        for num in nums:
            old_num = num
            num = bin(num)[2:]
            num = "0"*(length-len(num))+num
            curr = trie
            for i in num:
                curr = curr.setdefault(i, {})
            curr['#'] = old_num

        max_xor = 0
        for num in nums:
            num = bin(num)[2:]
            num = "0"*(length-len(num))+num
            curr = trie
            ans = 0
            for i in num:
                not_i = '1' if i == '0' else '0'
                ans <<= 1
                if not_i in curr:
                    ans += 1
                    curr = curr[not_i]
                else:
                    curr = curr[i]
            max_xor = max(max_xor, ans)
        return max_xor


nums = [3,10,5,25,2,8]
# Output: 28

nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127

sol = Solution()
print(sol.findMaximumXOR(nums))
