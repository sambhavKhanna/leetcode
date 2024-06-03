"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
def isValidSudoku(self, board: List[List[str]]) -> bool:
    def validate_square(row, col) -> bool:
        index_x = 3 * col
        index_y = 3 * row
        nums = set()
        for i in range(3):
            index_x = 3 * col
            for j in range(3):
                c = board[index_y][index_x]
                if c != '.' and c in nums:
                    return False
                elif c != '.':
                    nums.add(c)
                index_x += 1
            index_y += 1
        return True
    def validate_column(col):
        nums = set()
        for row in range(9):
            c = board[row][col]
            if c != '.' and c in nums:
                return False
            elif c != '.':
                nums.add(c)
        return True
    def validate_row(row):
        nums = set()
        for col in range(9):
            c = board[row][col]
            if c != '.' and c in nums:
                return False
            elif c != '.':
                nums.add(c)
        return True
    for _ in range(9):
        row = _ // 3
        col = _ % 3
        check = validate_row(_) and validate_column(_) and validate_square(row, col)
        if not check:
            print(_)
            print(validate_row(_))
            print(validate_column(_))
            print(validate_square(row, col))
            return False
    return True