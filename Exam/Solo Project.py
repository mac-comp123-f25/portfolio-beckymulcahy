"""Making a large flower that user input can change the color and number of petals"""

import turtle
import math

def color_input(question, default):
    color = input(f"{question} [default: {default}]: ").strip().lower()
    if not color:
        return default
    return color

def user_input(question, default, min_value, max_value):
    try:
        val = int(input(f"{question} [{default}]: ").strip() or default)
        if val < min_value or val > max_value:
            print(f"Using default ({default}) since {val} is out of range.")
            return default
        return val
    except:
        print ("Invalid input.")
        return default

def draw_single_petal(t, petal_color, petal_size, angle):
    t.color(petal_color)
    t.begin_fill()
    for _ in range(2):
        t.circle(petal_size, angle)
        t.left(180 - angle)
    t.end_fill()


def draw_petals(t, petal_color, center_color, num_petals, petal_size):
    for i in range(num_petals):
        draw_single_petal(t, petal_color, petal_size, 60)
        t.left(360 / num_petals)

    t.penup()
    t.goto(0, -petal_size * 0.2)
    t.pendown()
    t.color(center_color)
    t.begin_fill()
    t.circle(petal_size * 0.3)
    t.end_fill()



def main():
    print("Create your own flower!")

    petal_color = color_input("Enter petal color", "blue")
    center_color = color_input("Enter center color", "lightblue")
    num_petals = user_input("Enter number of petals (5–30)", 12, 5, 30)
    petal_size = user_input("Enter petal size (50–200)", 120, 50, 200)

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Here is your flower!")

    t = turtle.Turtle()
    t.speed(3)
    t.width(2)
    t.penup()
    t.goto(0, 0)
    t.pendown()

    draw_petals(t, petal_color, center_color, num_petals, petal_size)

    print("Drawing stem...")
    t.right(90)
    t.color("green")
    t.pensize(10)
    t.forward(petal_size * 1.5)

    print("Flower complete! Close the window to finish.")
    screen.mainloop()


if __name__ == "__main__":
    main()

