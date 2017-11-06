import turtle


def draw_z():
    # drawing alphabet z
    z = turtle.Turtle()
    z.speed(8)
    z.color("orange")

    z.up()
    z.left(90)
    z.forward(100)
    z.right(90)
    z.down()
    # drawing starts
    z.forward(58)
    z.right(122)
    z.forward(117)
    z.left(122)
    z.forward(62)

    # check
    '''
    z.left(90)
    z.forward(100)
    '''
    z.hideturtle()
# =================================
