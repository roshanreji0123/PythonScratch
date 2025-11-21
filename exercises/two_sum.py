def twoSum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return [-1, -1]


print(twoSum([2,7,11,15], 9))  # prints [0, 1]
