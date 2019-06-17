import arcade
import time


WIDTH = 50



grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Connect Four"


curr = True
x_chips = [0]*len(grid)

def switchTeam(x):
    global curr
    if curr:
        grid[0][x] = 1
        curr = False
    else:
        grid[0][x] = 2
        curr = True



def win():
    boardHeight = len(grid[0])
    boardWidth = len(grid)

    if curr:
        tile = 2
    else:
        tile = 1

    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if tile != 0 and grid[x][y] == tile and grid[x + 1][y] == tile and grid[x + 2][y] == tile and grid[x + 3][ y] == tile:
                team(curr)
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if  tile != 0 and grid[x][y] == tile and grid[x][y + 1] == tile and grid[x][y + 2] == tile and grid[x][y + 3] == tile:
                team(curr)
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if tile != 0 and grid[x][y] == tile and grid[x + 1][y - 1] == tile and grid[x + 2][y - 2] == tile and grid[x + 3][y - 3] == tile:
                team(curr)
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            tile = grid[x-1][y-1]
            if tile != 0 and grid[x][y] == tile and grid[x + 1][y + 1] == tile and grid[x + 2][y + 2] == tile and grid[x + 3][y + 3] == tile:
                team(curr)
                return True



class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.shape_list = None
        self.radius = 20





    def on_draw(self):
        """
        Render the screen.
        """
        if not win():
            arcade.start_render()
            margin_x = SCREEN_WIDTH//2 - WIDTH*2
            margin_y = SCREEN_HEIGHT//2 - WIDTH*2

            for i in range(len(grid)):
                for j in range(len(grid[i])):

                    x_chips[j] = (margin_x + j*WIDTH)

                    arcade.draw_rectangle_filled(margin_x + i*WIDTH, margin_y*2 + -j *WIDTH, WIDTH, WIDTH, arcade.color.WHITE)

                    if grid[j][i] == 0:
                        arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y*2 + -j*WIDTH, WIDTH//2, arcade.color.BLACK)

                    if grid[j][i] == 1:
                        arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y*2 +-j*WIDTH, WIDTH//2, arcade.color.RED)

                    if grid[j][i] == 2:
                        arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y*2 + -j*WIDTH, WIDTH//2, arcade.color.BLUE)



    def draw(self):
        return False not in [j != 0 for i in grid for j in i]


def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":

    main()
    print(x_chips)