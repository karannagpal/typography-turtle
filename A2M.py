import turtle


def draw_b():
    # draw a b shape
    b = turtle.Turtle()
    b.speed(8)
    b.color("yellow")

    b.up()
    b.forward(130)
    b.down()

    b.left(90)
    b.forward(150)
    b.right(90)
    b.forward(20)
    for ba in range(45):
        b.forward(2.5)
        b.right(4)
    b.forward(20)
    b.right(180)
    b.forward(25)
    for ba in range(45):
        b.forward(2.7)
        b.right(4)
    b.forward(25)

    b.hideturtle()
# =================================


def draw_c():
    # drawing alphabet c
    c = turtle.Turtle()
    c.speed(8)
    c.color("white")

    c.up()
    c.forward(200)
    c.down()

    c.left(90)
    c.up()
    c.forward(100)
    c.right(90)
    c.forward(60)
    c.right(180)
    # drawing starts here
    c.down()
    c.forward(15)
    for ca in range(9):
        c.forward(7)
        c.left(10)
    c.forward(20)
    for ca in range(9):
        c.forward(7)
        c.left(10)
    c.forward(22)

    c.hideturtle()
# ========


def draw_k():
    # drawing alphabet z
    k = turtle.Turtle()
    k.speed(8)
    k.color("lime")

    k.left(90)
    k.forward(100)
    k.up()
    k.right(180)
    k.forward(50)
    k.left(135)
    k.down()
    # first leg
    k.forward(70)
    k.up()
    k.backward(65)
    k.down()
    k.right(88)
    # second leg
    k.forward(77)

    # checking
    '''
    k.right(137)
    k.forward(60)
    k.right(90)
    k.forward(100)
    '''

    # k.hideturtle()
# =================================
