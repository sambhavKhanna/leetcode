"""
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
"""

def removeStars(self, s: str) -> str:
    stack = []
    p = 0
    while p < len(s):
        if s[p] == '*':
            stack.pop()
        else:
            stack.append(s[p])
        p += 1
    return ''.join(stack)