import turtle


def draw_space():
    space = turtle.Turtle()
    space.speed(8)
    space.color("cyan")

    # space.up()
    space.forward(40)
    space.hideturtle()
    return


def draw_dot():
    dot = turtle.Turtle()
    dot.speed(8)
    dot.color("orange")

    for dota in range(36):
        dot.forward(0.5)
        dot.left(10)
    return


def draw_dash():
    dash = turtle.Turtle()
    dash.speed(8)
    dash.color("yellow")
    return
