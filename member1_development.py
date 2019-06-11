
# check horizontal spaces
for y in range(boardHeight):
    for x in range(boardWidth - 3):
        if tile != 0 and grid[x][y] == tile and grid[x + 1][y] == tile and grid[x + 2][y] == tile and grid[x + 3][ y] == tile:
            team(curr)
            return True

# check vertical spaces
for x in range(boardWidth):
    for y in range(boardHeight - 3):
        if  tile != 0 and grid[x][y] == tile and grid[x][y + 1] == tile and grid[x][y + 2] == tile and grid[x]
            [y + 3] == tile:
            team(curr)
            return True

# check / diagonal spaces
for x in range(boardWidth - 3):
    for y in range(3, boardHeight):
        if tile != 0 and grid[x][y] == tile and grid[x + 1][y - 1] == tile and grid[x + 2][y - 2] == tile and grid[x + 3][y - 3] == tile:
            team(curr)
            return True