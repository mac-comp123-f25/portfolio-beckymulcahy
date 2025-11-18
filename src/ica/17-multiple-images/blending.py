from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def scale_up(image):
    old_width = image.getWidth()
    old_height = image.getHeight()

    new_width = old_width * 2
    new_height = old_height * 2

    new_pic = Picture(new_width, new_height)
    for x in range(new_width):
        for y in range(new_height):
            src_x = x // 2
            src_y = y // 2

            src_pixel = image.get_pixel(src_x, src_y)
            tgt_pixel = new_pic.get_pixel(x, y)

            tgt_pixel.red = src_pixel.red
            tgt_pixel.green = src_pixel.green
            tgt_pixel.blue = src_pixel.blue
    return new_pic



