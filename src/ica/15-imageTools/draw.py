from src.ica.helpers.dummyWindow import *
file_path = pickAFile()
print(file_path)

file_path = pickAFile()
image = Picture(file_path)
image.show()

pic1 = Picture("../SampleImages/butterfly.jpg")
pic1.show()

pic2 = Picture("../SampleImages/mightyMidway.jpg")
pic2.show()

pic3 = Picture("../SampleImages/bryceCanyon.jpg")
pic3.show()



def draw_something():
    picture = picture.open("../SampleImages/mightyMidway.jpg")

    width, height = picture.size
    num_pixels = width * height
    print(f"Number of pixels in the image: {num_pixels}")

    # Make a copy
    new_picture = picture.copy()
    pixels = new_picture.load()

    # Define red
    red = (255, 0, 0)

    # Change corner pixels to red
    pixels[0, 0] = red  # top-left
    pixels[width - 1, 0] = red  # top-right
    pixels[0, height - 1] = red  # bottom-left
    pixels[width - 1, height - 1] = red  # bottom-right


def main():
    drawing = draw_something()
    drawing.show()  # Open in default image viewer

    return new_picture

    ...


def main():
    drawing = draw_something()
    drawing.show()

    keep_windows_open()


if __name__ == "__main__":
    main()
