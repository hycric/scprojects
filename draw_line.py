"""
File: draw_line.py
Name: Richard Huang
-------------------------
TODO: This function draws circles and lines initiated by mouse clicks.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 15
window = GWindow()

# global variable
# Because: Can't input function and variables at the same time
count = 0
x0 = 0
y0 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(create_circle)


def create_circle(mouse):
    global count, x0, y0
    if count % 2 == 0:
        circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        # to make sure that the x,y of the mouse is at the center of the circle
        window.add(circle)
        x0 = mouse.x   # define x0, y0 as the coordinates of the circle
        y0 = mouse.y   # define x0, y0 as the coordinates of the circle
        count += 1
    else:
        circle1 = window.get_object_at(x0, y0)
        window.remove(circle1)
        count += 1
        line = GLine(x0, y0, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
