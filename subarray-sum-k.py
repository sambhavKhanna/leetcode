"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
def subarraySum(self, nums: List[int], k: int) -> int:
    cursum = 0
    counter = 0
    sums = {}
    for num in nums:
        cursum += num
        diff = cursum -k
        if cursum == k:
            counter += 1
        if diff in sums:
            counter += sums[diff]
        sums[cursum] = sums.get(cursum, 0) + 1
    return counter