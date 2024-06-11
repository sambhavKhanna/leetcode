"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

"""
def longestSubarray(self, nums: List[int]) -> int:
    l, r = 0, 0
    numOnes = 0
    maxLen = 0
    while r < len(nums):
        windowLen = r -l +1
        if nums[r] == 1: numOnes += 1
        if numOnes +1 < windowLen:
            if nums[l] == 1: numOnes -= 1
            l += 1
        else:
            maxLen = max(maxLen, windowLen)
        r += 1
    return maxLen -1