"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(space_ship, figure):  # 重疊兩張照片
    for x in range(space_ship.width):
        for y in range(space_ship.height):
            g = figure.get_pixel(x, y)
            s = space_ship.get_pixel(x, y)
            bigger = max(g.red, g.blue)  # 取出兩輸入值較大者
            if g.green <= bigger * 2:  # 根據條件式 輸出 pixel
                s.red = g.red
                s.green = g.green
                s.blue = g.blue
    return space_ship


def main():
    """
    TODO:
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
