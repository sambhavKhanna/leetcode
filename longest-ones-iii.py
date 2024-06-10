"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

def longestOnes(self, nums: List[int], k: int) -> int:
    l, r = 0, 0
    window = {}
    maxLen = 0
    while r < len(nums):
        window[nums[r]] = window.get(nums[r], 0) + 1
        windowLen = r -l +1
        maxOnes = window.get(1, 0) +k 
        if windowLen > maxOnes:
            window[nums[l]] -= 1
            l += 1
        else:
            maxLen = max(windowLen, maxLen)
        r += 1
    return maxLen