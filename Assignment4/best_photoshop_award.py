"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""


from simpleimage import SimpleImage

THRESHOLD1 = 1.2  # 解決顏色 問題
BLACK = 100  # 解決黑色 問題


def main():
    """
    TODO:
    """
    fig = SimpleImage('image_contest/IMG_1497.JPG')
    bg = SimpleImage('image_contest/brick_wall.jpeg')
    bg.make_as_big_as(fig)
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue)//3
            total = (fig_pixel.red + fig_pixel.green + fig_pixel.blue)
            if fig_pixel.green > avg * THRESHOLD1 and total > BLACK:
                # Green screen
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


if __name__ == '__main__':
    main()
# 創作理念：
# 很開心能夠參加 stanCode SC001 的課程。
# 背景是在 Stanford 網站上找到的牆壁。想藉由"紅磚"的元素 to show respect to Stanford and stanCode.
