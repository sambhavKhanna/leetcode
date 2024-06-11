"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
"""

def closeStrings(self, word1: str, word2: str) -> bool:
    hash1 = {}
    occurence1 = {}
    hash2 = {}
    occurence2 = {}
    for c in word1:
        hash1[c] = hash1.get(c, 0) +1
    for key in hash1.keys():
        occurence1[hash1[key]] = occurence1.get(hash1[key], 0) +1
    for c in word2:
        if c not in hash1:
            return False
        hash2[c] = hash2.get(c, 0) +1
    for key in hash2.keys():
        occurence2[hash2[key]] = occurence2.get(hash2[key], 0) +1
    for key in occurence2.keys():
        if key not in occurence1 or occurence1[key] != occurence2[key]:
            return False
    for key in occurence1.keys():
        if key not in occurence2 or occurence1[key] != occurence2[key]:
            return False
    return True