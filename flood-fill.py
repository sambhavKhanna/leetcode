"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

"""

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    m = len(image)
    n = len(image[0])
    start_color = image[sr][sc]

    if start_color == color:
        return image

    def helper(row, col):
        if image[row][col] == start_color:
            image[row][col] = color
            if row >= 1:
                helper(row - 1, col)
            if row < m - 1:
                helper(row + 1, col)
            if col >= 1:
                helper(row, col - 1)
            if col < n - 1:
                helper(row, col + 1)

    helper(sr, sc)
    return image