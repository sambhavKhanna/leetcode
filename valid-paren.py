"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    hash = {')':'(', ']': '[', '}': '{'}
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i in hash and hash[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if stack == []:
        return True
    return False