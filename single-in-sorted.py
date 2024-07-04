"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

def singleNonDuplicate(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) -1
    while l <= r:
        m = (l + r) // 2
        if m == 0 or m == len(nums) -1:
            return nums[m]
        if nums[m -1] == nums[m]:
            if (m -l) % 2 == 0:
                r = m -2
            else: l = m +1
        elif nums[m +1] == nums[m]:
            if (m -l) % 2 == 0:
                l = m +2
            else: r = m -1
        else:
            return nums[m]