"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""
def findPeakElement(self, nums: List[int]) -> int:
    def condition(m: int):
        if m == 0:
            if m == len(nums) -1:
                return 0
            if nums[m] > nums[m +1]:
                return 0
            return 1
        elif m == len(nums) -1:
            if nums[m] > nums[m -1]:
                return 0
            return -1
        elif nums[m -1] < nums[m] and nums[m] > nums[m +1]:
            return 0
        elif nums[m -1] < nums[m] and nums[m] < nums[m +1]:
            return 1
        elif nums[m -1] > nums[m] and nums[m] > nums[m +1]:
            return -1
        return 1
    l = 0
    r = len(nums) -1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        c = condition(m)
        if c == 0:
            ans = m
            break
        elif c == 1:
            l = m +1
        else:
            r = m -1
    return ans