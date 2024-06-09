"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.
"""

def isPalindrome(self, x: int) -> bool:
    ans = 0
    if x < 0: return False
    z = x
    while z > 0:
        ans = (10 * ans) + (z % 10)
        z = z // 10
    print(ans)
    return ans == x