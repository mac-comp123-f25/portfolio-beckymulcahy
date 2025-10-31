import turtle

def draw_nested_squares(tt):
    for side_length in range (10,80,10):
        for square in range (4):
            tt.forward(side_length)
            tt.right(90)

win = turtle.Screen()
tt = turtle.Turtle()
draw_nested_squares(tt)
win.exitonclick()