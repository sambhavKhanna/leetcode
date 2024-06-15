"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def sum(nums):
        sum = 0
        for i in nums:
            sum += i
        return sum
    total_sum = sum(nums)
    acc = 0
    for i in range(len(nums)):
        if 2 * acc == total_sum - nums[i]:
            return i
        acc += nums[i]
    return -1