import turtle


def draw_a(offset):
    # drawing alphabet a
    a = turtle.Turtle()
    a.speed(5)
    a.color("red")

    a.up()
    a.forward(offset)
    a.down()

    a.left(78)
    a.forward(108)
    a.right(146)
    a.forward(108)
    a.backward(40)
    a.right(112)
    a.forward(36)

    a.hideturtle()


def draw_b(offset):
    # draw b shape
    b = turtle.Turtle()
    b.speed(8)
    b.color("yellow")

    b.up()
    b.forward(offset)
    b.down()

    b.left(90)
    b.forward(100)
    b.right(90)
    b.forward(8)
    for ba in range(18):
        b.forward(4.2)
        b.right(10)
    b.forward(10)
    b.right(180)
    b.forward(12)
    for ba in range(18):
        b.forward(4.5)
        b.right(10)
    b.forward(18)

    b.hideturtle()


def draw_c(offset):
    # drawing alphabet c
    c = turtle.Turtle()
    c.speed(8)
    c.color("white")
    c.pensize(2)

    c.up()
    c.forward(offset)
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


def draw_d(offset):
    # drawing alphabet d
    d = turtle.Turtle()
    d.speed(1)
    d.color("white")

    d.up()
    d.forward(offset)
    d.down()

    d.right(90)
    d.forward(50)
    d.right(90)
    d.circle(-50 / 2, -180, 30)

    d.hideturtle()


def draw_e(offset):
    # drawing alphabet e
    e = turtle.Turtle()
    e.speed(5)
    e.color("lime")

    e.up()
    e.forward(offset)
    e.down()

    e.left(90)
    e.forward(100)
    e.right(90)
    e.forward(60)
    e.backward(60)
    e.right(90)
    e.forward(50)
    e.left(90)
    e.forward(40)
    e.backward(40)
    e.right(90)
    e.forward(50)
    e.left(90)
    e.forward(60)

    e.hideturtle()


def draw_f(offset):
    # drawing alphabet f
    f = turtle.Turtle()
    f.speed(5)
    f.color("lime")

    f.up()
    f.forward(offset)
    f.down()

    f.left(90)
    f.forward(100)
    f.right(90)
    f.forward(60)
    f.backward(60)
    f.right(90)
    f.forward(50)
    f.left(90)
    f.forward(40)
    f.backward(40)
    f.right(90)

    f.hideturtle()


def draw_g(offset):
    g = turtle.Turtle()
    g.speed(5)
    g.color('yellow')

    g.up()
    g.forward(offset)
    g.down()

    return


def draw_h(offset):
    # drawing alphabet h
    h = turtle.Turtle()
    h.speed(2)
    h.color("white")

    h.up()
    h.forward(offset)
    h.down()

    h.right(90)
    h.forward(50)
    h.backward(50 / 2)
    h.left(90)
    h.forward(50)
    h.right(90)
    h.backward(50 / 2)
    h.forward(50)

    h.hideturtle()


def draw_i(offset):
    # drawing alphabet i
    i = turtle.Turtle()
    i.speed(1)
    i.color("lime")

    i.up()
    i.forward(offset)
    i.down()

    i.forward(50)
    i.backward(50 / 2)
    i.left(90)
    i.forward(50)
    i.left(90)
    i.forward(50 / 2)
    i.backward(50)

    i.hideturtle()


def draw_j(offset):
    # drawing alphabet j
    j = turtle.Turtle()
    j.speed(5)
    j.color("white")

    j.up()
    j.forward(offset)
    j.down()

    return


def draw_k(offset):
    # drawing alphabet z
    k = turtle.Turtle()
    k.speed(8)
    k.color("lime")

    k.up()
    k.forward(offset)
    k.down()

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
    k.hideturtle()
    return


def draw_l(offset):
    # drawing alphabet l
    l = turtle.Turtle()
    l.speed(1)
    l.color("lime")

    l.up()
    l.forward(offset)
    l.down()

    l.left(90)
    l.forward(50)
    l.backward(50)
    l.right(90)
    l.forward(50)

    l.hideturtle()
    return


def draw_m(offset):
    # drawing alphabet m
    m = turtle.Turtle()
    m.speed(1)
    m.color("lime")

    m.up()
    m.forward(offset)
    m.down()

    m.left(90)
    m.forward(50)
    m.right(150)
    m.forward(57)
    m.left(120)
    m.forward(57)
    m.right(150)
    m.forward(50)

    m.hideturtle()
    return
