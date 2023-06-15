def maxsubarray(nums:list[int]) -> int:
    maxsum=nums[0]
    currentsum=0
    for i in nums:
        if currentsum<0:
            currentsum=0
        currentsum+=i
        maxsum = max(maxsum,currentsum)
    return maxsum

print(maxsubarray([-2,-3,-4,-5,-2,-3,-6,-7]))