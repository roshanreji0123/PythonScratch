def moveZeroes(nums):
    j = 0  

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums

print(moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
