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



class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.shape_list = None
        self.radius = 20


    def update(self, dt):
        """ Move everything """
        index = len(grid[0])-1
        # for i in range(len(grid)):
        #     if grid[i][index] == 1 and grid[i][index-1] != 0:
        #         continue
        #     else:
        #         grid[i][index] = 0
        #         grid[i][index-1] = 1


    def on_key_press(self, symbol: int, modifiers: int):
        keys = [49 + i for i in range(len(grid[0]))]
        for i in range(len(keys)):
            if symbol == keys[i] and grid[0][i] == 0:
                switchTeam(i)

    def win():
        boardHeight = len(grid[0])
        boardWidth = len(grid)
        tile = 2 if curr else 1

        # check horizontal spaces
        for y in range(boardHeight):
            for x in range(boardWidth - 3):
                if tile != 0 and grid[x][y] == tile and grid[x + 1][y] == tile and grid[x + 2][y] == tile and \
                        grid[x + 3][
                            y] == tile:
                    team(curr)
                    return True

        # check vertical spaces
        for x in range(boardWidth):
            for y in range(boardHeight - 3):
                if tile != 0 and grid[x][y] == tile and grid[x][y + 1] == tile and grid[x][y + 2] == tile and grid[x][
                    y + 3] == tile:
                    team(curr)
                    return True


    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        margin_x = SCREEN_WIDTH//2  - WIDTH*2
        margin_y = SCREEN_HEIGHT//2 - WIDTH*2
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x_chips[i] = (margin_x + i*WIDTH)
                arcade.draw_rectangle_filled( margin_x+ i*WIDTH,margin_y + j *WIDTH,WIDTH, WIDTH, arcade.color.WHITE)
                if grid[i][j] == 0:
                    arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y + j*WIDTH, WIDTH//2, arcade.color.BLACK)
                if grid[i][j] == 1:
                    arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y + j*WIDTH, WIDTH//2, arcade.color.RED)
                if grid[i][j] == 2:
                    arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y + j*WIDTH, WIDTH//2, arcade.color.BLUE)



def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":

    main()
    print(x_chips)