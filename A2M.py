import turtle


def draw_a(offset):
    # drawing alphabet a
    a = turtle.Turtle()
    a.speed(5)
    a.color("pink")

    a.up()
    a.forward(offset)
    a.down()

    a.left(73.5)
    a.forward(103)
    a.right(2*73.5)
    a.forward(103)
    a.backward(40)
    a.right(180-73.5)
    a.forward(37)

    a.hideturtle()


def draw_b(offset):
    # draw b shape
    b = turtle.Turtle()
    b.speed(8)
    b.color("green")

    b.up()
    b.forward(offset)
    b.down()

    # check
    for ba in range(2):
        b.forward(60)
        b.left(90)
        b.forward(100)
        b.left(90)
    b.color('yellow')

    b.left(90)
    b.forward(100)
    b.right(90)
    b.forward(25)
    for ba in range(18):
        b.forward(4.35)
        b.right(10)
    b.forward(27)
    b.right(180)
    b.forward(27)
    for ba in range(18):
        b.forward(4.37)
        b.right(10)
    b.forward(32)

    b.hideturtle()


def draw_c(offset):
    # drawing alphabet c
    c = turtle.Turtle()
    c.speed(8)
    c.color("white")

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
    d.speed(5)
    d.color("wheat")

    d.up()
    d.forward(offset)
    d.down()

    d.left(90)
    d.forward(100)
    d.right(90)
    d.forward(15)
    for da in range(9):
        d.forward(7)
        d.right(10)
    d.forward(19)
    for da in range(9):
        d.forward(7.2)
        d.right(10)
    d.forward(22)

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
    e.forward(55)
    e.backward(55)
    e.right(90)
    e.forward(50)
    e.left(90)
    e.forward(45)
    e.backward(45)
    e.right(90)
    e.forward(50)
    e.left(90)
    e.forward(60)

    e.hideturtle()


def draw_f(offset):
    # drawing alphabet f
    f = turtle.Turtle()
    f.speed(5)
    f.color("lightblue")

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
    f.forward(45)

    f.hideturtle()


def draw_g(offset):
    g = turtle.Turtle()
    g.speed(9)
    g.color('orange')

    g.up()
    g.forward(offset)
    g.down()

    g.up()
    g.left(90)
    g.forward(100)
    g.right(90)
    g.forward(56)
    g.right(90)
    g.forward(5)
    g.right(180)
    g.down()
    # start
    g.left(40)
    for ga in range(5):
        g.forward(2)
        g.left(10)
    g.forward(20)
    for ga in range(9):
        g.forward(4.3)
        g.left(10)

    g.forward(50)

    for ga in range(9):
        g.forward(4.2)
        g.left(10)

    g.forward(11)

    for ga in range(9):
        g.forward(4.2)
        g.left(10)

    g.forward(25)
    g.left(90)
    g.forward(25)

    g.hideturtle()
    return


def draw_h(offset):
    # drawing alphabet h
    h = turtle.Turtle()
    h.speed(2)
    h.color("lime")

    h.up()
    h.forward(offset)
    h.down()

    h.left(90)
    h.forward(100)
    h.backward(50)
    h.right(90)
    h.forward(60)
    h.left(90)
    h.forward(50)
    h.backward(100)

    h.hideturtle()


def draw_i(offset):
    # drawing alphabet i
    i = turtle.Turtle()
    i.speed(5)
    i.color("yellow")

    i.up()
    i.forward(offset)


    i.forward(5)
    i.down()

    i.left(90)
    i.forward(100)

    i.hideturtle()


def draw_j(offset):
    # drawing alphabet j
    j = turtle.Turtle()
    j.speed(5)
    j.color("white")

    j.up()
    j.forward(offset)
    j.down()

    j.left(90)

    j.up()
    j.forward(100)
    j.right(90)
    j.forward(60)
    j.down()
    j.right(90)
    j.forward(68)
    for ja in range(18):
        j.forward(5.2)
        j.right(10)
    j.forward(10)
    j.hideturtle()
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

    k.hideturtle()
    return


def draw_l(offset):
    # drawing alphabet l
    l = turtle.Turtle()
    l.speed(5)
    l.color("lime")

    l.up()
    l.forward(offset)
    l.down()

    l.left(90)
    l.forward(100)
    l.backward(100)
    l.right(90)
    l.forward(60)

    l.hideturtle()
    return


def draw_m(offset):
    # drawing alphabet m
    m = turtle.Turtle()
    m.speed(5)
    m.color("lime")

    m.up()
    m.forward(offset)
    m.down()

    m.left(90)
    m.forward(100)
    m.right(150)
    m.forward(80)
    m.left(120)
    m.forward(80)
    m.right(150)
    m.forward(100)

    m.hideturtle()
    return
