def count_neighbours(grid, row, col):
    sum = 0
    if row-1 >= 0:
        sum = sum + grid[row-1][col]
    if col-1 >= 0:
        sum = sum + grid[row][col-1]
    if row-1 >= 0 and col-1 >= 0:
        sum = sum + grid[row-1][col-1]
    if row+1 < len(grid):
        sum = sum + grid[row+1][col]
    if col+1 < len(grid[0]):
        sum = sum + grid[row][col+1]
    if row+1 < len(grid) and col+1 < len(grid[0]):
        sum = sum + grid[row+1][col+1]
    if row-1 >= 0 and col+1 < len(grid[0]):
        sum = sum + grid[row-1][col+1]
    if row+1 < len(grid) and col-1 >= 0:
        sum = sum + grid[row+1][col-1]
    #print sum
    return sum


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #print count_neighbours(((1, 0, 0, 1, 0),(0, 1, 0, 0, 0),(0, 0, 1, 0, 1),(1, 0, 0, 0, 0),(0, 0, 1, 0, 0),), 1, 2)
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
