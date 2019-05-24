
import arcade

WIDTH = 100
HEIGHT= 100

MARGIN = 15

ROW_COUNT = 6
COLUMN_COUNT = 7

grid = []

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

def on_update(delta_time):
   pass

def on_draw():
   arcade.start_render()
   # Draw in here...
   for row in range(ROW_COUNT):
       for column in range(COLUMN_COUNT):
           if grid[row][column] == 1:
               color = arcade.color.GREEN
           else:
               color = arcade.color.WHITE

           x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
           y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
           arcade.draw_circle_filled(x, y, WIDTH, HEIGHT, color)

def on_key_press(key, modifiers):
   pass

def on_key_release(key, modifiers):
   pass

def on_mouse_press(x, y, button, modifiers):
    pass

def setup():
   global grid
   arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Connect Four")
   arcade.set_background_color(arcade.color.BLACK)
   arcade.schedule(on_update, 1/60)
   # Override arcade window methods
   window = arcade.get_window()
   window.on_draw = on_draw
   window.on_key_press = on_key_press
   window.on_key_release = on_key_release
   window.on_mouse_press = on_mouse_press
   # create a 10 x 10 2D list of numbers
   # --- Populate grid the grid
   # Loop for each row
   for row in range(ROW_COUNT):
       # For each row, create a list that will
       # represent an entire row
       grid.append([])
       # Loop for each column
       for column in range(COLUMN_COUNT):
           # Add a the number zero to the current row
           grid[row].append(0)

   arcade.run()

if __name__ == '__main__':
   setup()

