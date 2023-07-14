"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(old_img):
    b_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            b_p = b_img.get_pixel(x, y)
            if x and y > 0:  # x, y 需要大於0 故設立條件式
                pix_a = old_img.get_pixel(x - 1, y - 1)  # (x,y) 為九宮格中心 pix_abcdeghi 分別為九宮格由上到下的 pixel。
            if y > 0:
                pix_b = old_img.get_pixel(x, y - 1)
                if x != 299:  # 雖然 x,y 最大值等於 299 但是因為 +1 會導致 300, 故需要設立條件式
                    pix_c = old_img.get_pixel(x + 1, y - 1)
            if x > 0:
                pix_d = old_img.get_pixel(x - 1, y)
                if y != 299:
                    pix_g = old_img.get_pixel(x - 1, y + 1)
            if x != 299:
                pix_f = old_img.get_pixel(x + 1, y)
            if y != 299:
                pix_h = old_img.get_pixel(x, y + 1)
            if x != 299 and y != 299:
                pix_i = old_img.get_pixel(x + 1, y + 1)
            if x == 0 and y == 0:  # 原點
                avr = (pix_f.red + pix_h.red + pix_i.red) // 3
                avg = (pix_f.green + pix_h.green + pix_i.green) // 3
                avb = (pix_f.blue + pix_h.blue + pix_i.blue) // 3
                b_p.red = avr
                b_p.green = avg
                b_p.blue = avb
            if x == 0 and y != 0:  # X軸
                if y != b_img.height - 1:
                    avr = (pix_b.red + pix_c.red + pix_f.red + pix_h.red + pix_i.red) // 5
                    avg = (pix_b.green + pix_c.green + pix_f.green + pix_h.green + pix_i.green) // 5
                    avb = (pix_b.blue + pix_c.blue + pix_f.blue + pix_h.blue + pix_i.blue) // 5
                    b_p.red = avr
                    b_p.green = avg
                    b_p.blue = avb
                else:  # 左下角
                    avr = (pix_b.red + pix_c.red + pix_f.red) // 3
                    avg = (pix_b.green + pix_c.green + pix_f.green) // 3
                    avb = (pix_b.blue + pix_c.blue + pix_f.blue) // 3
                    b_p.red = avr
                    b_p.green = avg
                    b_p.blue = avb

            if x == b_img.width - 1 and y == 0:  # 右上角
                avr = (pix_d.red + pix_g.red + pix_h.red) // 3
                avg = (pix_d.green + pix_g.green + pix_h.green) // 3
                avb = (pix_d.blue + pix_g.blue + pix_h.blue) // 3
                b_p.red = avr
                b_p.green = avg
                b_p.blue = avb

            if x == b_img.width - 1 and y != 0:  # 右極限 X 軸
                if y != b_img.height - 1:
                    avr = (pix_a.red + pix_b.red + pix_d.red + pix_g.red + pix_h.red) // 5
                    avg = (pix_a.green + pix_b.green + pix_d.green + pix_g.green + pix_h.green) // 5
                    avb = (pix_a.blue + pix_b.blue + pix_d.blue + pix_g.blue + pix_h.blue) // 5
                    b_p.red = avr
                    b_p.green = avg
                    b_p.blue = avb
                else:  # 右下角
                    avr = (pix_a.red + pix_b.red + pix_d.red) // 3
                    avg = (pix_a.green + pix_b.green + pix_d.green) // 3
                    avb = (pix_a.blue + pix_b.blue + pix_d.blue) // 3
                    b_p.red = avr
                    b_p.green = avg
                    b_p.blue = avb
            if x > 0 and y == 0:  # y = 0
                avr = (pix_d.red + pix_f.red + pix_g.red + pix_h.red + pix_i.red) // 5
                avg = (pix_d.green + pix_f.green + pix_g.green + pix_h.green + pix_i.green) // 5
                avb = (pix_d.blue + pix_f.blue + pix_g.blue + pix_h.blue + pix_i.blue) // 5
                b_p.red = avr
                b_p.green = avg
                b_p.blue = avb
            if x > 0 and y == b_img.height - 1:  # y = height
                avr = (pix_a.red + pix_b.red + pix_c.red + pix_d.red + pix_f.red) // 5
                avg = (pix_a.green + pix_b.green + pix_c.green + pix_d.green + pix_f.green) // 5
                avb = (pix_a.blue + pix_b.blue + pix_c.blue + pix_d.blue + pix_f.blue) // 5
                b_p.red = avr
                b_p.green = avg
                b_p.blue = avb
            if 0 < x < b_img.width and 0 < y < b_img.height:  # 9宮格
                avr = (pix_a.red + pix_b.red + pix_c.red + pix_d.red + pix_f.red + pix_g.red + pix_h.red
                       + pix_i.red) // 8
                avg = (pix_a.green + pix_b.green + pix_c.green + pix_d.green + pix_f.green + pix_g.green + pix_h.green
                       + pix_i.green) // 8
                avb = (pix_a.blue + pix_b.blue + pix_c.blue + pix_d.blue + pix_f.blue + pix_g.blue + pix_h.blue
                       + pix_i.blue) // 8
                b_p.red = avr
                b_p.green = avg
                b_p.blue = avb
    return b_img


if __name__ == '__main__':
    main()
