"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
"""

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def lessOrEqual(k):
        if k < 0:
            return 0
        l, r = 0, 0
        numNice = 0
        ans = 0
        while r < len(nums):
            if nums[r] % 2 == 1:
                numNice += 1
            while numNice > k:
                if nums[l] % 2 == 1:
                    numNice -= 1
                l += 1
            ans = ans +r -l +1
            r += 1
        return ans
    return lessOrEqual(k) -lessOrEqual(k -1)
