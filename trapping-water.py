"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

"""
def trap(self, height: List[int]) -> int:
    area = 0
    maxes = []
    max_left = 0
    max_right = 0
    for i in range(len(height)):
        if i == 0:
            maxes.append(0)
        else:
            maxes.append(max_left)
        max_left = max(max_left, height[i])
    for i in range(len(height) -1, -1, -1):
        minheight = min(maxes[i], max_right)
        if minheight > height[i]:
            area += minheight - height[i]
        max_right = max(height[i], max_right)
    return area