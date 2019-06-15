import arcade
import time

WIDTH = 50
HEIGHT = 50

state = 0
grid = []
temp = []
n = 1
for i in range(8):
   if len(temp) > 1:
       grid.append(temp)
   temp = []
   for j in range(6):
       temp.append(0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Connect Four"
team = True
curr = True
x_chips = [0] * len(grid)
y_chips = [0] * len(grid[1])



class MyGame(arcade.Window):
      """ Main application class. """

      def __init__(self):
          super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
          self.shape_list = None
          self.radius = 20

      def closest(self, x):
          d = x
          l = x_chips
          n = ([abs(i - d) for i in l])
          return (n.index(min(n)))

      def get_y(self, x_clicked):
          l = grid[x_clicked]
          n = 0
          for i in l:
              if i == 0:
                  return (n)
                  break
              n += 1

      def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
          global curr
          global state
          if state == 0:
              x_clicked = (self.closest(x))
              y_empty = self.get_y(x_clicked)
              if curr == True:
                  grid[x_clicked][y_empty] = 2
                  curr = False
              else:
                  grid[x_clicked][y_empty] = 1
                  curr = True




      def on_draw(self):
          """
          Render the screen.
          """
          arcade.start_render()
          margin_x = 155
          margin_y = 180
          for i in range(len(grid)):
              for j in range(len(grid[i])):
                  x_chips[i] = (margin_x + i * WIDTH)
                  y_chips[j] = (margin_y + j * HEIGHT)



                  arcade.draw_rectangle_filled(margin_x + i * WIDTH, margin_y + j * WIDTH, WIDTH, WIDTH,
                                               arcade.color.WHITE)
                  if grid[i][j] == 0:
                      arcade.draw_circle_filled(margin_x + i * WIDTH, margin_y + j * WIDTH, WIDTH // 2,
                                                arcade.color.BLACK)
                  if grid[i][j] == 1:
                      arcade.draw_circle_filled(margin_x + i * WIDTH, margin_y + j * WIDTH, WIDTH // 2,
                                                arcade.color.RED)
                  if grid[i][j] == 2:
                      arcade.draw_circle_filled(margin_x + i * WIDTH, margin_y + j * WIDTH, WIDTH // 2,
                                               arcade.color.BLUE)

def main():
    window = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()