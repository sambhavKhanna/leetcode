"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

def characterReplacement(self, s: str, k: int) -> int:
    window = {}
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        window[i] = 0
    l, r = 0, 0
    maxLen = 0
    while r < len(s):
        window[s[r]] = window.get(s[r], 0) +1
        windowLen = r -l +1
        maxChar = max(window, key=window.get)
        maxFreq = window[maxChar]
        if windowLen > maxFreq +k:
            window[s[l]] -= 1
            l += 1
        else:
            maxLen = max(maxLen, windowLen)
        r += 1
    return maxLen