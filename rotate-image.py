"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    length = len(matrix)
    origin = 0, 0
    while length > 1:
        x, y = origin
        for i in range(length -1):
            temp = matrix[x +i][y +length -1]
            matrix[x +i][y +length -1] = matrix[x][y +i]
            matrix[y +length -1][x +length -i -1], temp = temp, matrix[y +length -1][x +length -i -1]
            matrix[y +length -i -1][x], temp = temp, matrix[y +length -i -1][x]
            matrix[x][y +i] = temp
        length -= 2
        x += 1
        y += 1
        origin = x, y