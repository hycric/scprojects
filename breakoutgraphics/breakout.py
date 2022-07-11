"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    """
    This game is called Breakout. In this game, the player has to try his/her best to clear out all bricks and avoid
    losing the ball towards the bottom of the window.
    """
    graphics = BreakoutGraphics()   # Names the BreakoutGraphics function graphics
    life = NUM_LIVES                # An indicator that indicates the number of lives left in the game.

    while life > 0:                 # When there are more than 1 lives left the game contineus
        dx = graphics.get_dx()      # Retrieves the value of dx
        dy = graphics.get_dy()      # Retrieves the value of dy
        pause(FRAME_RATE)           # Slows down the movement speed of the ball
        pause(FRAME_RATE)
        graphics.ball.move(dx, dy)  # Allows the ball to move per loop
        if graphics.ball.x < 0:
            graphics.set_dx(-dx)    # Changes the x direction of the ball when collides with window.

        elif graphics.ball.x + graphics.ball.width > graphics.window.width:
            graphics.set_dx(-dx)

        elif graphics.ball.y < 0:
            graphics.set_dy(-dy)    # Changes the y direction of the ball when collides with window.

        elif graphics.ball.y + graphics.ball.height > graphics.window.height:
            life -= 1               # Minus 1 life everytime ball goes below bottom window.
            if life <= 0:
                graphics.ball.x = graphics.window.width / 2 - graphics.ball.width / 2
                graphics.ball.y = graphics.window.height / 2 - graphics.ball.height / 2


            else:
                graphics.ball.x = graphics.window.width / 2 - graphics.ball.width / 2
                graphics.ball.y = graphics.window.height / 2 - graphics.ball.height / 2
                pause(2000)         # Time for the user to prepare for the next round

        for i in range(0, 2):       # Double for loop used to detect collision with objects(paddle, brick)
            for j in range(0, 2):
                x_bar = graphics.ball.x + graphics.ball.width * j
                y_bar = graphics.ball.y + graphics.ball.height * i
                obj = graphics.window.get_object_at(x_bar, y_bar)
                if obj:             # Either hits paddle or hit brick.
                    if obj is not graphics.paddle:
                        graphics.window.remove(obj)
                        graphics.set_dy(-dy)
                    else:
                        graphics.set_dy(-dy)
                    break


if __name__ == '__main__':
    main()
