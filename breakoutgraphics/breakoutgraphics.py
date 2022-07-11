"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

"""
This Class is called BreakoutGraphics. 
Provides all the constants and functions needed for the game "Breakout".
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=window_width / 2 - paddle_width / 2,
                            y=window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width / 2 - ball_radius,
                          y=window_height / 2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        def paddle_move(mouse):
            if 0 + self.paddle.width / 2 <= mouse.x <= window_width - self.paddle.width / 2:
                self.paddle.x = mouse.x - self.paddle.width / 2

        onmousemoved(paddle_move)

        def on_switch(mouse):  # Sets up the initial velocity of the ball and avoids multi clicks during motion
            if self.ball.x == window_width / 2 - ball_radius and self.ball.y == window_height / 2 - ball_radius:
                self.__dy = INITIAL_Y_SPEED
                self.__dx = random.randint(1, MAX_X_SPEED)
                if random.random() > 0.5:
                    self.__dx = -self.__dx

        onmouseclicked(on_switch)

        # Draw bricks
        x_z = 0
        y_z = 0
        color_list = ['red', 'orange', 'green', 'yellow', 'blue']
        col_count = 0  # The count of bricks per row.
        row_count = 0  # The count of row of the same color.
        color = 0      # The integer that decides the color of the row.
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                x_z = BRICK_WIDTH * j + BRICK_SPACING * j
                y_z = BRICK_HEIGHT * i + BRICK_SPACING * i
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=x_z, y=y_z)
                brick.filled = True
                col_count += 1
                if row_count < 2:
                    brick.fill_color = color_list[color]
                if col_count == 10:
                    row_count += 1
                    col_count = 0
                if row_count == 2:
                    color += 1
                    row_count = 0
                self.window.add(brick)

    # Getter functions

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy
