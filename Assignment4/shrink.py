"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage




def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink(original)
    after_shrink.show()


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    img_p = filename
    b_img = SimpleImage.blank(img_p.width//2, img_p.height//2) # Create Blank Img
    for x in range(b_img.width):
        for y in range(b_img.height):
            i_p = img_p.get_pixel(2*x, 2*y) # 因為 長寬 都要所小 1/2 所以 pixel 用 2的倍數 去跑
            b_p = b_img.get_pixel(x, y)
            b_p.red = i_p.red
            b_p.green = i_p.green
            b_p.blue = i_p.blue
    return b_img



if __name__ == '__main__':
    main()
