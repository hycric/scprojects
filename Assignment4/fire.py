"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""

from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def main():
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires(original_fire)
    highlighted_fire.show()


def highlight_fires(filename):

    for pixel in filename:
        avg = (pixel.red + pixel.blue + pixel.green)//3  # 取某 pixel 之 RGB 平均值
        if pixel.red > avg * HURDLE_FACTOR:  # 若符合條件 則調整色調
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return filename


if __name__ == '__main__':
    main()
