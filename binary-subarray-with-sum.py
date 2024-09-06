"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
"""

def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    def lessOrEqual(goal):
        if goal < 0:
            return 0
        l, r = 0, 0
        cursum = 0
        ans = 0
        while r < len(nums):
            cursum += nums[r]
            while cursum > goal:
                cursum -= nums[l]
                l += 1
            ans = ans + r -l +1
            r += 1
        return ans
    return lessOrEqual(goal) -lessOrEqual(goal -1)