"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""
def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = []
    for i in nums1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in nums2:
        if i in d and d[i] > 0:
            ans.append(i)
            d[i] -= 1
    return ans