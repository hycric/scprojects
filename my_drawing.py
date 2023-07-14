"""
File: my_drawing.py
Name: Richard Huang
----------------------
TODO: Draws a person wearing a hat and a stanCode T-shirt.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    This program draws a person wearing a hat and a stanCode T-shirt.
    """
    window = GWindow(width=800, height=500, title='Spartan')
    head = GOval(100, 100, x=350, y=50)
    head.filled = True
    head.fill_color = 'bisque'
    l_eye = GOval(15, 25, x=370, y=72)
    l_eye_1 = GOval(7, 7, x=374, y=80)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    l_eye_1.filled = True
    r_eye = GOval(15, 25, x=415, y=72)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    r_eye_1 = GOval(7, 7, x=419, y=80)
    r_eye_1.filled = True
    nose = GOval(12, 20, x=392.5, y=93)
    mouth = GArc(40, 20, 190, 180, x=380, y=120)
    l_ear = GArc(35, 25, 88, 200, x=339, y=93)
    l_ear.filled = True
    l_ear.fill_color = "bisque"
    r_ear = GArc(35, 25, 254, 204, x=439, y=93)
    r_ear.filled = True
    r_ear.fill_color = "bisque"
    l_neck = GLine(382, 146, 382, 160)
    stancode = GLabel("stanCode", x=395, y=200)
    stancode.font = '-8'
    l_shoulder = GLine(382, 160, 342, 170)
    l_shirt = GLine(342, 170, 332, 250)
    l_shirt_1 = GLine(332, 250, 353, 245)
    l_shirt_2 = GLine(353, 245, 363, 190)
    l_body = GLine(363, 190, 363, 260)
    r_neck = GLine(418, 146, 418, 160)
    r_shoulder = GLine(418, 160, 458, 170)
    r_shirt = GLine(458, 170, 468, 250)
    r_shirt_1 = GLine(468, 250, 447, 245)
    r_shirt_2 = GLine(447, 245, 437, 190)
    r_body = GLine(437, 190, 437, 260)
    body = GLine(363, 260, 437, 260)
    l_pants = GLine(363, 260, 363, 370)
    l_pants_1 = GLine(363, 370, 380, 370)
    l_pants_2 = GLine(380, 370, 400, 290)
    r_pants = GLine(437, 260, 437, 370)
    r_pants_1 = GLine(437, 370, 420, 370)
    r_pants_2 = GLine(420, 370, 400, 290)
    l_shoe = GRect(30, 13, x=350, y=370)
    l_shoe.filled = True
    l_shoe.fill_color = 'lavender'
    r_shoe = GRect(30, 13, x=420, y=370)
    r_shoe.filled = True
    r_shoe.fill_color = 'lavender'
    l_hand = GOval(16, 16, x=335, y=249)
    l_hand.filled = True
    l_hand.fill_color = 'bisque'
    r_hand = GOval(16, 16, x=451, y=249)
    r_hand.filled = True
    r_hand.fill_color = 'bisque'
    top_hat = GRect(80, 40, x=360, y=20)
    top_hat.filled = True
    top_hat.fill_color = 'lavender'
    bot_hat = GRect(120, 10, x=340, y=50)
    bot_hat.filled = True
    bot_hat.fill_color = 'lavender'
    window.add(head)
    window.add(l_eye)
    window.add(l_eye_1)
    window.add(r_eye)
    window.add(r_eye_1)
    window.add(nose)
    window.add(mouth)
    window.add(l_ear)
    window.add(r_ear)
    window.add(l_neck)
    window.add(r_neck)
    window.add(stancode)
    window.add(l_shoulder)
    window.add(r_shoulder)
    window.add(l_shirt)
    window.add(l_shirt_1)
    window.add(l_shirt_2)
    window.add(l_body)
    window.add(r_shirt)
    window.add(r_shirt_1)
    window.add(r_shirt_2)
    window.add(r_body)
    window.add(body)
    window.add(l_pants)
    window.add(l_pants_1)
    window.add(l_pants_2)
    window.add(r_pants)
    window.add(r_pants_1)
    window.add(r_pants_2)
    window.add(l_shoe)
    window.add(r_shoe)
    window.add(l_hand)
    window.add(r_hand)
    window.add(top_hat)
    window.add(bot_hat)


# 創作理念：因為一開始上課時有做人臉，想說就把整個人也做出來，並且塗上我喜歡的顏色（淡紫色）：）。


if __name__ == '__main__':
    main()
