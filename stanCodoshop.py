"""
File: stanCodoshop.py
Name: Richard Huang
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    rt = 0                  # Pixel List 中 所有 red pixel值的總和
    gt = 0                  # Pixel List 中 所有 green pixel值的總和
    bt = 0                  # Pixel List 中 所有 blue pixel值的總和
    rgb = []
    for pix in pixels:      # List 的 迴圈用來加總個pixel rgb 值
        rt += pix.red
        gt += pix.green
        bt += pix.blue
    red = rt//len(pixels)   # 算出 rgb 單值的 avg
    green = gt//len(pixels)
    blue = bt//len(pixels)
    rgb.append(red)
    rgb.append(green)
    rgb.append(blue)        # append 至 空 list "rgb" 上
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance",
    which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    l_avg = get_average(pixels)
    #candidates = []                         # 用來存放 各 pixel_dist 的 list
    dist = 0
    dist_f = float('inf')
    for p in pixels:
        dist = get_pixel_dist(p, l_avg[0], l_avg[1], l_avg[2])
        if dist < dist_f:
            dist_f = dist
            best = p
    return best
    #     #candidates.append(get_pixel_dist(p, l_avg[0], l_avg[1], l_avg[2]))
    # best_dist = min(candidates)             # 用來求出 candidates 這個list 中 pixel_dist 最小值
    # index = candidates.index(best_dist)     # 回推出 此pixel_dist 所屬的index
    # return pixels[index]                    # 回傳 pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width                     # 設立 空白頁面 之後存放pixel 用
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    # pixels = []                                 # 設立 pixel list 存放每一組pixel資料
    # for x in range(width):
    #     for y in range(height):
    for pixel in result:
        pixels = []
        for image in images:
            pix = image.get_pixel(pixel.x, pixel.y)
            pixels.append(pix)
        best = get_best_pixel(pixels)           # 取得最佳pixel
        goal = result.get_pixel(pixel.x, pixel.y)
        goal.red = best.red                     # 把best --> 貼上 blank image "result" 上
        goal.green = best.green
        goal.blue = best.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
