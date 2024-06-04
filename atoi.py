"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""

def myAtoi(self, s: str) -> int:
    int_min = -2 ** 31
    int_max = 2 ** 31 -1
    int_upto_max = int_max // 10
    int_max_ones = int_max % 10
    int_min_ones = int_max_ones +1 
    accept = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    preprocess = ""
    saw_digit = False
    sign = False
    integer = 0
    for c in s:
        if c == '-' and not saw_digit:
            saw_digit = True
            sign = True
        elif c == '+' and not saw_digit:
            saw_digit = True
        elif c not in accept and not saw_digit:
            if c == ' ': pass
            else: break
        elif c not in accept and saw_digit:
            break
        else:
            if integer > int_upto_max and sign:
                integer = int_min
                sign = False
                break
            elif integer > int_upto_max and not sign:
                integer = int_max
                break
            elif integer == int_upto_max and sign:
                if int(c) >= int_min_ones:
                    integer = int_min
                    sign = False
                    break
            elif integer == int_upto_max and not sign:
                if int(c) >= int_max_ones:
                    print("HI", int(c), int_max_ones)
                    integer = int_max
                    break
            integer = 10 * integer + int(c)
            saw_digit = True
    return -integer if sign else integer