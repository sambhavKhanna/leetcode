"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""

def findMaxLength(self, nums: List[int]) -> int:
    count1, count0 = 0, 0
    maxLen = 0
    hash = {}
    for i in range(len(nums)):
        if nums[i] == 0:
            count0 += 1
        else:
            count1 += 1
        diff = count1 -count0
        if count1 == count0:
            maxLen = max(maxLen, 2 * count0)
        elif diff in hash:
            j = hash[diff]
            maxLen = max(maxLen, i -j)
        if diff not in hash:
            hash[diff] = i
    return maxLen