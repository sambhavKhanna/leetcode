"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

def convert(self, s: str, numRows: int) -> str:
    matrix = [[] for row in range(numRows)]
    up = False
    vertical = 0
    for _ in s:
        if vertical <= 0:
            vertical = 0
            matrix[vertical].append(_)
            up = False
            vertical += 1
        elif vertical >= numRows -1:
            vertical = numRows -1
            matrix[vertical].append(_)
            up = True
            vertical -= 1
        elif up:
            matrix[vertical].append(_)
            vertical -= 1
        else:
            matrix[vertical].append(_)
            vertical += 1
    ans = ''.join([''.join(row) for row in matrix])
    return ans