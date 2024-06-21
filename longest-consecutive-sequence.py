"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

def longestConsecutive(self, nums: List[int]) -> int:
    hash = set(nums)
    curmax = 0
    for num in nums:
        if num -1 in hash:
            continue
        else:
            itrnum = num
            running_max = 0
            while itrnum in hash:
                running_max += 1
                itrnum += 1
            curmax = max(curmax, running_max)
    return curmax