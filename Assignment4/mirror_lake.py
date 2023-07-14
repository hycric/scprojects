"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage





def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect(original_mt)
    reflected.show()


def reflect(filename):
    b_img = SimpleImage.blank(filename.width, filename.height*2)  # 設立 空白照片 高度 是 原本照片的兩倍
    b_img.show()
    for x in range(filename.width):
        for y in range(filename.height):
            # colored
            img_p = filename.get_pixel(x, y)

            # blank1
            b_p1 = b_img.get_pixel(x, y)
            # blank2
            b_p2 = b_img.get_pixel(x, b_img.height - 1 - y)  # 設計 對稱 座標

            b_p1.red = img_p.red
            b_p1.green = img_p.green
            b_p1.blue = img_p.blue

            b_p2.red = img_p.red
            b_p2.green = img_p.green
            b_p2.blue = img_p.blue
    return b_img


if __name__ == '__main__':
    main()
