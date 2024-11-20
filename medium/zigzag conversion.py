def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    grid = [[[]] for i in range(numRows)]
    row = 0
    column = 0
    movement_row = 1
    for letter in s:
        grid[row][column].append(letter)
        if row == numRows-1:
            movement_row = -1
            movement_column = 1
        elif row == 0:
            movement_row = 1
            movement_column = 0
        row += movement_row
    word = ''
    for row_num in range(len(grid)):
        for letter in grid[row_num][0]:
            word += letter
    return word

print(convert("ABC",1))