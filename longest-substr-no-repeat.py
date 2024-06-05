"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""
def lengthOfLongestSubstring(self, s: str) -> int:
    curstr = {}
    minindex = 0
    curmax = 0
    for i in range(len(s)):
        if s[i] not in curstr or curstr[s[i]] < minindex:
            pass
        else:
            minindex = curstr[s[i]] + 1
        curstr[s[i]] = i
        curmax = max(curmax, i - minindex + 1)
    return curmax