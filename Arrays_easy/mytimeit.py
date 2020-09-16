import timeit

# code snippet to be executed only once
# mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''
def twoSum(numbers: [int], target: int) -> [int]:
    begining, end = 0, len(numbers)-1
    while begining < end:
        if numbers[end] + numbers[begining] == target:
            return [begining+1, end+1]
        elif numbers[end] + numbers[begining] > target:
            end -= 1
        else:
            begining += 1

numbers = [2,7,11,15]
target = 9
twoSum(numbers, target)
'''

# timeit statement
print(timeit.timeit(stmt = mycode, number = 10000))


# code snippet to be executed only once
# mysetup = "from math import "

# code snippet whose execution time is to be measured
mycode = '''
def twoSum(numbers: [int], target: int) -> [int]:
    begining, end = 0, len(numbers)-1
    while begining < end:
        left = numbers[begining]
        right = numbers[end]
        if left + right == target:
            return [begining+1, end+1]
        elif left + right > target:
            end -= 1
        else:
            begining += 1

numbers = [2,7,11,15]
target = 9
twoSum(numbers, target)
'''

# timeit statement
print(timeit.timeit(stmt = mycode, number = 10000))


# # code snippet to be executed only once
# mysetup = "from math import "

# code snippet whose execution time is to be measured
mycode = '''
def twoSum(numbers: [int], target: int) -> [int]:
    begining, end = 0, len(numbers)-1
    while begining < end:
        if numbers[end] + numbers[begining] == target:
            return [begining+1, end+1]
        elif numbers[end] + numbers[begining] > target:
            end -= 1
        else:
            begining += 1

numbers = [2,7,11,15]
target = 9
twoSum(numbers, target)
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
