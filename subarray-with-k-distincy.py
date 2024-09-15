"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
"""

def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    def lessThanEqual(k):
        if k == 0:
            return 0
        l, r = 0, 0
        count = 0
        window = {}
        while r < len(nums):
            window[nums[r]] = window.get(nums[r], 0) +1
            while len(window) > k:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
            count = count + r -l +1
            r += 1
        return count
    return lessThanEqual(k) -lessThanEqual(k -1)