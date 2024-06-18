"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
"""

def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    ans = []
    for i in spells:
        l = 0
        r = len(potions) -1
        number = 0
        while l <= r:
            m = (l + r) // 2
            product = i * potions[m]
            left_product = i * potions[l]
            right_product = i * potions[r]
            if success <= left_product:
                number = len(potions) -l
                break
            if success > right_product:
                number = len(potions) -r -1
                break
            if product < success:
                l = m +1
            else:
                r = m -1
        ans.append(number)
    return ans