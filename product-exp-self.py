"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(1)
        else:
            result.append(result[i -1] * nums[i -1])
    running_mul = 1
    for i in range(len(result) -1, -1, -1):
        if i == len(result) -1:
            running_mul = nums[i]
        else:
            result[i] *= running_mul
            running_mul *= nums[i]
    return result  