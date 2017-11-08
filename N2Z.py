import turtle


def draw_n():
    # drawing alphabet n
    n = turtle.Turtle()
    n.speed(8)
    n.color("cyan")

    n.left(90)
    n.forward(100)
    n.right(149)
    n.forward(116)
    n.left(149)
    n.forward(100)
    '''
    # checking
    n.left(90)
    n.forward(60)
    n.left(90)
    n.forward(100)
    '''
    n.hideturtle()


def draw_o():
    # drawing alphabet o
    o = turtle.Turtle()
    o.speed(8)
    o.color("cyan")

    o.left(90)
    o.up()
    o.forward(50)
    o.down()
    o.forward(20)
    for oa in range(18):
        o.right(10)
        o.forward(5.3)
    o.forward(40)
    for oa in range(18):
        o.right(10)
        o.forward(5.3)
    o.forward(20)

    # checking
    '''
    o.forward(50)
    o.right(90)
    o.forward(60)
    o.right(90)
    o.forward(100)
    '''
    o.hideturtle()


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
