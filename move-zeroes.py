"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    s, f = 0, 0
    while f < len(nums):
        if nums[f]:
            nums[s], nums[f] = nums[f], nums[s]
            s += 1
        f +=1