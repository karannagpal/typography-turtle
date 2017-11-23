import turtle


def draw_space(offset):
    space = turtle.Turtle()
    space.speed(8)

    space.up()
    space.forward(offset + 40)
    space.down()

    space.hideturtle()
    return


def draw_dot(offset):
    dot = turtle.Turtle()
    dot.speed(8)
    dot.color("orange")
    dot.up()
    dot.forward(offset)
    dot.down()

    for a_dot in range(36):
        dot.forward(0.7)
        dot.left(10)

    dot.hideturtle()
    return


def draw_dash(offset):
    dash = turtle.Turtle()
    dash.speed(8)
    dash.color("yellow")
    dash.up()
    dash.forward(offset)
    dash.down()

    dash.left(90)
    dash.up()
    dash.forward(45)
    dash.right(90)
    dash.forward(15)
    dash.down()
    dash.forward(30)
    dash.up()
    dash.forward(15)

    dash.hideturtle()
    return
