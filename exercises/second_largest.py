#second_largest.py
def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')

    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n

    return second
