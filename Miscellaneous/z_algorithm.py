'''
z algorithm
'''

class ZAlgorithm:

    def calculateZ(self, inp):

        z = [0]*len(inp)
        left, right = 0, 0
        for k in range(1, len(inp)):
            if k > right:
                left = right = k
                while right < len(inp) and inp[right] == inp[right-left]:
                    right += 1
                z[k] = right - left
                right -= 1
            else:
                # we are operating inside box
                k1 = k - left
                # if value does not stretches till right bound then just copy it.
                if z[k1] < right - k + 1 :
                    z[k] = z[k1]
                else: #otherwise try to see if there are more matches.
                    left = k
                    while right < len(inp) and inp[right] == inp[right - left]:
                        right += 1
                    z[k] = right - left
                    right -= 1
        return z
    
    # Returns list of all indices where pattern is found in text.
    def matchPattern(self, text, pattern):
        newString = [0]*(len(text)+len(pattern)+1)
        i = 0
        for c in pattern:
            newString[i] = c
            i += 1
        newString[i] = '$'
        i += 1
        for c in text:
            newString[i] = c
            i += 1
        
        result = []
        z = self.calculateZ(newString)
        print(z)
        
        for i in range(len(z)):
            if z[i] == len(pattern):
                result.append(i - len(pattern) - 1)

        return result

text = "aaabcxyzaaaabczaaczabbaaaaaabc"
pattern = "aaabc"

# text = "aabxaabxcaacxaabxay"
# pattern = "aa"

# text = 'xabcabzabc'
# pattern = 'abc'

obj = ZAlgorithm()
res = obj.matchPattern(text, pattern)
print(res)
