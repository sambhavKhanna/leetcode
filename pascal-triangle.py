"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

def generate(self, numRows: int) -> List[List[int]]:
    ans = [[1]]
    while numRows > 1:
        newList = [1]
        for i, j in zip(ans[-1], ans[-1][1:]):
            newList.append(i +j)
        newList.append(1)
        ans.append(newList)
        numRows -= 1
    return ans