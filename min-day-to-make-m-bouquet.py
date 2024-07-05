"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
"""
def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    def check_day(day):
        num_bouquet = 0
        i = 0
        while num_bouquet < m and i < len(bloomDay):
            num_flower = 0
            while num_flower < k and i < len(bloomDay):
                if bloomDay[i] > day:
                    i += 1
                    break
                num_flower += 1
                i += 1
            if num_flower == k:
                num_bouquet += 1
                
        return num_bouquet == m

    max_day = max(bloomDay)
    l = 1
    r = max_day
    min_day = -1

    while l <= r:
        mid = (l + r) // 2
        if check_day(mid):
            if min_day == -1:
                min_day = mid
            else:
                min_day = min(min_day, mid)
            r = mid -1
        else:
            l = mid +1
    return min_day