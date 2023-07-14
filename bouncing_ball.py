"""
File: 
Name: Richard Huang
-------------------------
TODO: Displays the movement of a ball drop. The ball drop starts by the user clicking on the mouse. Then moves both
horizontally and vertically in the window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 6
DELAY = 30  # originally 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball.filled = 'True'
    window.add(ball)
    onmouseclicked(on_switch)


def on_switch(mouse):
    global ball
    ongoing = 0  # 確保球是否在動作中
    if ongoing == 0:  # 如果求不在動作中 滑鼠點擊 會使 球開始彈跳
        if ball.x == START_X and ball.y == START_Y:
            ongoing = 1  # 彈跳同時 把 變數 改成 1 使 excess mouse click 不影響 movement
            count = 0  # 記 球彈出 匡外的次數 三次 就會 跳出Loop
            vy = 0  # 垂直速度 初速 為 0
            while True:
                vy += GRAVITY
                ball.move(VX, vy)
                if ball.x + SIZE >= window.width and ball.y + SIZE >= window.height:  # 當球體超出 匡外 並且 落地使 開始記數
                    count += 1
                    if count == 3:
                        ball = window.get_object_at(ball.x, ball.y)   # 找出超出匡外的球
                        window.remove(ball)    # removes the ball outside of the window area
                        ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
                        ball.filled = 'True'
                        window.add(ball)
                        ongoing = 0   # 使開關 重回 起始值
                        break
                if ball.y + SIZE >= window.height:  # 當球出界時 確保 反彈不會再次觸及 底線以外的區域 設立的判別式
                    if ball.y + (-vy) * REDUCE < window.height:
                        vy = (-vy) * REDUCE
                pause(DELAY)
        else:
            pass


if __name__ == "__main__":
    main()
