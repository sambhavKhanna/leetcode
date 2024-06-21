"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

def replaceElements(self, arr: List[int]) -> List[int]:
    p = len(arr) -1
    rev = []
    curmax = 0
    while p >= 0:
        if p == len(arr) -1:
            curmax = arr[p]
            rev.append(-1)
        else:
            rev.append(curmax)
            curmax = max(arr[p], curmax)
        p -= 1
    rev.reverse()
    return rev