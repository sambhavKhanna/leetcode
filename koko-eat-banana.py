"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def is_valid_k(k):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / k)
        if total_time <= h:
            return True
        return False
    max_element = max(piles)
    l = 1
    r = max_element
    k = max_element
    while l <= r:
        m = (l + r) // 2
        if is_valid_k(m):
            k = min(m, k)
            k = m
            r = m -1
        else:
            l = m +1
    return k