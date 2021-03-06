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
       for y in range(3, boardHeight):
           tile = grid[x-1][y-1]
           if tile != 0 and grid[x][y] == tile and grid[x + 1][y + 1] == tile and grid[x + 2][y + 2] == tile and grid[x + 3][y + 3] == tile:
               team(curr)
               return True

def team(won):

   if not won:

       arcade.draw_text("Red Team Won", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 100,
                        arcade.color.RED if not won else arcade.color.BLUE
                        , 52, font_name='GARA')
   else:
       arcade.draw_text("Blue Team Won", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 100,
                        arcade.color.RED if not won else arcade.color.BLUE
                        , 52, font_name='GARA')




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
           margin_x = 180
           margin_y = 220

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
       arcade.draw_text("Use your number 1-6 keys to play.", 220, 150, arcade.color.WHITE, 10)
       arcade.draw_text("Each number corresponds with a column,", 200, 139, arcade.color.WHITE, 10)
       arcade.draw_text("for example the first column from the left is 1 and so on.", 160, 128, arcade.color.WHITE, 10)

   def draw(self):
       return False not in [j != 0 for i in grid for j in i]


def main():
   window = MyGame()
   arcade.run()


if __name__ == "__main__":

   main()
   print(x_chips)
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
       for y in range(3, boardHeight):
           tile = grid[x-1][y-1]
           if tile != 0 and grid[x][y] == tile and grid[x + 1][y + 1] == tile and grid[x + 2][y + 2] == tile and grid[x + 3][y + 3] == tile:
               team(curr)
               return True

def team(won):

   if not won:

       arcade.draw_text("Red Team Won", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 100,
                        arcade.color.RED if not won else arcade.color.BLUE
                        , 52, font_name='GARA')
   else:
       arcade.draw_text("Blue Team Won", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 100,
                        arcade.color.RED if not won else arcade.color.BLUE
                        , 52, font_name='GARA')




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
           margin_x = 180
           margin_y = 220

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
       arcade.draw_text("Use your number 1-6 keys to play.", 220, 150, arcade.color.WHITE, 10)
       arcade.draw_text("Each number corresponds with a column,", 200, 139, arcade.color.WHITE, 10)
       arcade.draw_text("for example the first column from the left is 1 and so on.", 160, 128, arcade.color.WHITE, 10)

   def draw(self):
       return False not in [j != 0 for i in grid for j in i]


def main():
   window = MyGame()
   arcade.run()


if __name__ == "__main__":

   main()
   print(x_chips)

