"""
File: babygraphics.py
Name: Richard Huang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    a = width - GRAPH_MARGIN_SIZE * 2  # applicable total space
    b = a // len(YEARS)  # increments
    x = GRAPH_MARGIN_SIZE + b * year_index
    return x


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Base Line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    # Top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)

    # Vertical Lines
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH, fill='black')
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    count = 0
    inc = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)
    base = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
    for name in lookup_names:       # 按照所輸入的名字清單 執行迴圈一一展示折線圖
        index = 0
        if count == 4:
            count = 0
        c = COLORS[count]
        count += 1
        dct2 = name_data[name]      # 某人名字 各年的資訊
        print(name_data['Jennifer'])
        for yr in YEARS:
            yr = str(yr)
            if yr in dct2:
                rk = int(dct2[yr])  # 用yr 為 key 引出該年的名次
                yr2 = str(int(yr) + 10)
                if yr2 in dct2:
                    rk1 = int(dct2[yr2])  # 因為 要畫線需要兩個點因此下一年的高度也需要求出來
                    x = get_x_coordinate(CANVAS_WIDTH, index)  # 找到那一年的 x 軸 起點
                    x1 = x + inc
                    canvas.create_line(x, rk*.6 + GRAPH_MARGIN_SIZE, x1, rk1*.6 + GRAPH_MARGIN_SIZE, fill=c, width=LINE_WIDTH)
                    canvas.create_text(x + TEXT_DX, rk*.6 + GRAPH_MARGIN_SIZE, text=name + " " + str(rk),
                                       anchor=tkinter.SW, fill=c)
                else:
                    if int(yr2) in YEARS:  # 防止線超過2010
                        x = get_x_coordinate(CANVAS_WIDTH, index)
                        x1 = x + inc
                        canvas.create_line(x, rk*.6, x1, base, fill=c, width=LINE_WIDTH)
                        canvas.create_text(x + TEXT_DX, rk*.6 + GRAPH_MARGIN_SIZE, text=name + " " + '*', anchor=tkinter.SW, fill=c)
                    else:
                        canvas.create_text(x + TEXT_DX, rk*.6 + GRAPH_MARGIN_SIZE, text=name + " " + str(rk),
                                           anchor=tkinter.SW, fill=c)
            else:  # rk for that yr > 1000:
                x = get_x_coordinate(CANVAS_WIDTH, index)
                yr2 = str(int(yr) + 10)
                if yr2 in dct2:  # 第二點 < 1000
                    rk1 = int(dct2[yr2])
                    x1 = x + inc
                    canvas.create_line(x, base, x1, rk1*.6 + GRAPH_MARGIN_SIZE, fill=c, width=LINE_WIDTH)
                else:  # 第二點 > 1000
                    if int(yr2) in YEARS:
                        x1 = x + inc
                        canvas.create_line(x, base, x1, base, fill=c, width=LINE_WIDTH)
                canvas.create_text(x + TEXT_DX, base, text=name + " " + '*', anchor=tkinter.SW, fill=c)
            index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
