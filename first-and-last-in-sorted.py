"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

def searchRange(self, nums: List[int], target: int) -> List[int]:
    low_bound = len(nums)
    l = 0
    r = len(nums) -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            low_bound = min(low_bound, m)
            r = m -1
        elif nums[m] < target:
            l = m +1
        else:
            r = m -1
    if low_bound == len(nums):
        return [-1, -1]
    up_bound = -1
    l = 0
    r = len(nums) -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            up_bound = max(up_bound, m)
            l = m +1
        elif nums[m] < target:
            l = m +1
        else:
            r = m -1
    return [low_bound, up_bound]