"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

def uniqueOccurrences(self, arr: List[int]) -> bool:
    hash = {}
    keys = set()
    for i in arr:
        hash[i] = hash.get(i, 0) +1
    for key in hash.keys():
        if hash[key] in keys:
            return False
        else: keys.add(hash[key])
    return True