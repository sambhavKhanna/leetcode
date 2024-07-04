"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""
def mySqrt(self, x: int) -> int:
    l = 0
    r = x
    ans = 0
    while l <= r:
        m = l + (r -l) // 2
        if m * m <= x:
            ans = max(ans, m)
            l = m +1
        else:
            r = m -1
    return ans