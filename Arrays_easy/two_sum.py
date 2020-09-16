class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        begining, end = 0, len(numbers)-1
        while begining < end:
            if numbers[end] + numbers[begining] == target:
                return [begining+1, end+1]
            elif numbers[end] + numbers[begining] > target:
                end -= 1
            else:
                begining += 1

obj = Solution()
numbers = [2,7,11,15]
target = 9
print(obj.twoSum(numbers, target))
numbers = [2,3,4]
target = 6
print(obj.twoSum(numbers, target))
numbers = [-1,0]
target = -1
print(obj.twoSum(numbers, target))

# from leetcode
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i
