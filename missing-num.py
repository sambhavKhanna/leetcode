"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    for i in range(len(nums) + 1):
        sum += i
    for i in nums:
        sum -= i
    return sum