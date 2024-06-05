"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    result = [0, False]
    for i in range(n):
        l = i +1
        r = n -1
        while l < r:
            candidate = nums[l] + nums[r] + nums[i]
            curdiff = abs(candidate -target)
            mindiff = abs(result[0] -target)
            if not result[1] or curdiff < mindiff:
                result[1] = True
                result[0] = candidate
            if candidate > target:
                r -= 1
            else:
                l += 1
    return result[0] 