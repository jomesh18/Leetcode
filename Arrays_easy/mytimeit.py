import timeit

# code snippet to be executed only once
# mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''
def longestCommonPrefix(strs: []) -> str:
    if len(strs) == 0: return ""
    prefix = ""
    sample = min(strs, key=len)
    word_count = len(strs)
    checks = 0

    for i in range(0, len(sample)):
        for string in strs:
            if sample[i] == string[i]:
                checks += 1
                continue
            else:
                return prefix
        if checks == word_count:
            prefix += sample[i]
            checks = 0
    return prefix

strs = ["flower","flow","flight"]
longestCommonPrefix(strs)
'''

# timeit statement
print(timeit.timeit(stmt = mycode, number = 10000))




# code snippet to be executed only once
# mysetup = "from math import "

# code snippet whose execution time is to be measured
mycode = '''
def longestCommonPrefix(strs: []) -> str:
    if len(strs) == 0: return ""
    min_len = len(min(strs, key=len))
    res = []
    common = True
    for j in range(min_len):
        for string in strs[1:]:
            if string[j] != strs[0][j]:
                common = False
                break
        if common:
            res.append(strs[0][j])
            j += 1
        else:
            return "".join(res)
    return "".join(res)

strs = ["flower","flow","flight"]
longestCommonPrefix(strs)
'''

# timeit statement
print(timeit.timeit(stmt = mycode, number = 10000))


# # code snippet to be executed only once
# mysetup = "from math import "

# code snippet whose execution time is to be measured
mycode = '''
def longestCommonPrefix(strs: []) -> str:
    if len(strs) ==0:
        return ""
    prefix = ""
    strs = sorted(strs,key=lambda x: len(x))
    first_word =strs[0]
    max_prefix = len(first_word)
    need_to_run =True
    index = 0
    last_index = 0
    while need_to_run and index < max_prefix:
        for word in strs[1:]:
            if word[index] !=first_word[index]:
                need_to_run=False
                last_index = index
        if need_to_run:
            prefix+=first_word[index]
        index+=1
    return prefix

strs = ["flower","flow","flight"]
longestCommonPrefix(strs)
'''

# timeit statement
print(timeit.timeit(stmt = mycode, number = 10000))



# # code snippet to be executed only once
# mysetup = "from math import "
#
# # code snippet whose execution time is to be measured
# mycode = '''
# def example():
#     mylist = []
#     for x in range(100):
#         mylist.append(sqrt(x))
# '''
#
# # timeit statement
# print(timeit.timeit(setup = mysetup,
#                     stmt = mycode,
#                     number = 10000))
