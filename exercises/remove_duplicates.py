#remove_duplicates.py


def remove_duplicates(nums):
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return result

nums = [10,10,30,30,40,20,60]
print(remove_duplicates(nums))
