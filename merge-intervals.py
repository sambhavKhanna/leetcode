"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: (x[0], x[1]))
    res = [intervals[0]]
    for i in intervals:
        if res[-1][0] <= i[0] and res[-1][1] >= i[1]:
            continue
        if res[-1][1] < i[0]:
            res.append(i)
        else:
            res[-1][1] = i[1]
    return res