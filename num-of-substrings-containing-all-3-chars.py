"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
"""

def numberOfSubstrings(self, s: str) -> int:
    l, r = 0, 0
    ans = 0
    strMap = {}
    while r < len(s):
        strMap[s[r]] = strMap.get(s[r], 0) +1
        while 'a' in strMap and 'b' in strMap and 'c' in strMap:
            ans = ans + len(s) -r
            strMap[s[l]] -= 1
            if strMap[s[l]] == 0:
                del strMap[s[l]]
            l += 1
        r += 1
    return ans