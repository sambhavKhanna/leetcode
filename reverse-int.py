"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

def reverse(self, x: int) -> int:
    int_max = 2 ** 31 -1
    int_min = -2 ** 31

    def length(x: int):
        if not x: return 1
        len = 0
        while x:
            len += 1
            x = x // 10
        return len
    def from_left(x: int, index: int):
        len = length(x) -1 -index
        return (x // 10 ** len) % 10
    def from_right(x: int, index: int):
        return (x // 10 ** index) % 10
    def out_of_bound(x: int, sign: bool):
        len = length(x)
        if length(x) < 10: return False
        if not sign:
            for i in range(len):
                l = from_left(int_max, i)
                r = from_right(x, i)
                if l < r:
                    return True
                elif l > r:
                    break
            return False
        else:
            for i in range(len):
                l = from_left(int_max, i)
                r = from_right(x, i)
                if l < r:
                    return True
                elif l > r:
                    break
                
            return False
    def reverse_normal(x: int):
        result = 0
        while x:
            result = 10 * result + (x % 10)
            x = x // 10
        return result
    if x < 0:
        if x == int_min:
            return 0
        if out_of_bound(-x, True):
            return 0
        return -reverse_normal(-x)
    if out_of_bound(x, False):
        return 0
    return reverse_normal(x)