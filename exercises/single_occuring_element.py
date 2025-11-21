def singleNumber(nums):
    result = 0
    for n in nums:
        result ^= n
    return result
print(singleNumber([3,3,2,2,4,1,1]))