"""
File: sierpinski.py
Name: Richard Huang
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6  # Controls the order of Sierpinski Triangle
LENGTH = 600  # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150  # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100  # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950  # The width of the GWindow
WINDOW_HEIGHT = 700  # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
    """
    TODO: This file draws a set of sierpinski triangles.
    """
    sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
    """
    Draws the sierspinski_triangle
    :param order: int, The sequential number that controls the pattern of the triangles
    :param length: int, the length of the triangle
    :param upper_left_x: int, the upper left x coordinate of the triangle
    :param upper_left_y: int, the upper left y coordinate of the triangle
    :return: object, a triangle
    """

    if order == 0:
        pass
    else:
        h = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
        r = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * .5, upper_left_y + length * .866)
        l = GLine(upper_left_x, upper_left_y, upper_left_x + length * .5, upper_left_y + length * .866)

        window.add(h)
        window.add(l)
        window.add(r)

        # Upper Left
        sierpinski_triangle(order-1, length*1/2, upper_left_x, upper_left_y)
        # Upper Right
        sierpinski_triangle(order-1, length*1/2, upper_left_x + length*1/2, upper_left_y)
        # Middle Bottom
        sierpinski_triangle(order-1, length*1/2, upper_left_x + length * 1/4, upper_left_y + length*1/2*.866)


if __name__ == '__main__':
    main()
