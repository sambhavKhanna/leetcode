"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i -1]:
            continue 
        l = i +1
        r = n -1
        target = -nums[i]
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l -1]:
                    l += 1
            elif sum < target:
                l += 1
            else:
                r -= 1
    return result