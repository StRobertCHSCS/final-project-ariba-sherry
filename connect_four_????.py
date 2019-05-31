from settings import *

x_chips = [0]*len(grid)

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



    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
            global curr
            for i in  range(len(x_chips)):
                if x_chips[i]-WIDTH<x < x_chips[i] and (button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_MIDDLE or button == arcade.MOUSE_BUTTON_RIGHT):
                    if curr:
                        grid[i][len(grid[0])-1] = 1
                        curr = False
                    else:
                        grid[i][len(grid[0])-1] = 2
                        curr = True




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