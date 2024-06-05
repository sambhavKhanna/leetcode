"""
Given a string s, return the longest 
palindromic substring in s.
"""

def longestPalindrome(self, s: str) -> str:
    maxstr = ""
    n = len(s)
    for i in range(n):
        l = i -1
        r = i +1
        curstr = s[i]
        while l >= 0 and r < n and s[l] == s[r]:
            curstr = s[l] + curstr + s[r]
            l -= 1
            r += 1
        if len(curstr) > len(maxstr):
            maxstr = curstr
    for i in range(n -1):
        if s[i] == s[i +1]:
            l = i -1
            r = i +2
            curstr = s[i] + s[i +1]
            while l >= 0 and r < n and s[l] == s[r]:
                curstr = s[l] + curstr + s[r]
                l -= 1
                r += 1
            if len(curstr) > len(maxstr):
                maxstr = curstr
    return maxstr