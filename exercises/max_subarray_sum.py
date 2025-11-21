def max_subarray_sum(nums):
    max_sum=float('-inf')
    current_sum=0
    for num in nums:
        current_sum+=num
        max_sum=max(max_sum,current_sum)
        if(current_sum<0):
            current_sum=0
    return max_sum
print(f"The max subarray sum is {max_subarray_sum([-1,-2,-3,4,5,-5,7,3,-1,2])}")
