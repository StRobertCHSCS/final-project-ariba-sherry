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

        # if no team has won

        if not win():
            if not self.draw():
                for i in range(1, len(grid)):
                    for j in range(len(grid[i])):
                        # check if after is empty slot
                        if grid[i-1][j] != 0 and grid[i][j] == 0:
                            # chip falls down
                            grid[i][j] = grid[i-1][j]
                            grid[i - 1][j] = 0
        else:
            time.sleep(1)
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid[i][j] = 0




    def on_key_press(self, symbol: int, modifiers: int):
        keys = [49 + i for i in range(len(grid[0]))]
        for i in range(len(keys)):
            if symbol == keys[i] and grid[0][i] == 0:
                switchTeam(i)



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