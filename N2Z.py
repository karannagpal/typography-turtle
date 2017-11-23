import turtle


def draw_n(offset):
    # drawing alphabet n
    n = turtle.Turtle()
    n.speed(8)
    n.color("pink")
    n.up()
    n.forward(offset)
    n.down()

    n.left(90)
    n.forward(100)
    n.right(149)
    n.forward(116)
    n.left(149)
    n.forward(100)

    n.hideturtle()


def draw_o(offset):
    # drawing alphabet o
    o = turtle.Turtle()
    o.speed(8)
    o.color("white")
    o.up()
    o.forward(offset)
    o.down()

    o.left(90)
    o.up()
    o.forward(51)
    o.down()
    o.forward(22)

    for oa in range(18):
        o.right(10)
        o.forward(5.25)

    o.forward(40)

    for oa in range(18):
        o.right(10)
        o.forward(5.25)

    o.forward(21)

    o.hideturtle()


def draw_p(offset):
    # draws alphabet p
    p = turtle.Turtle()
    p.speed(5)
    p.color('cyan')
    p.up()
    p.forward(offset)
    p.down()

    p.left(90)
    p.forward(100)
    p.right(90)
    p.forward(30)
    for pa in range(18):
        p.forward(4.5)
        p.right(10)
    p.forward(33)

    p.hideturtle()
    return


def draw_q(offset):
    # draws alphabet q
    q = turtle.Turtle()
    q.speed(5)
    q.color('yellow')
    q.up()
    q.forward(offset)
    q.down()

    q.left(90)
    q.up()
    q.forward(51)
    q.down()
    q.forward(22)

    for qa in range(18):
        q.right(10)
        q.forward(5.25)

    q.forward(40)

    for qa in range(18):
        q.right(10)
        q.forward(5.25)

    q.forward(21)

    q.up()
    q.right(180)
    q.forward(35)
    q.left(90)
    q.forward(38)
    q.down()

    q.right(45)
    q.forward(30)

    q.hideturtle()
    return


def draw_r(offset):
    # draws alphabet r
    r = turtle.Turtle()
    r.speed(5)
    r.color('orange')
    r.up()
    r.forward(offset)
    r.down()

    r.left(90)
    r.forward(100)
    r.right(90)

    r.forward(30)
    for ra in range(18):
        r.forward(4.5)
        r.right(10)

    r.forward(33)
    r.backward(15)

    r.left(132)
    r.forward(65)

    r.hideturtle()
    return


def draw_s(offset):
    # draws alphabet s
    s = turtle.Turtle()
    s.speed(5)
    s.color('lime')
    s.up()
    s.forward(offset)
    s.down()

    s.up()
    s.left(90)
    s.forward(100)
    s.right(90)
    s.forward(56)
    s.right(90)
    s.forward(5)
    s.right(180)
    s.down()

    # start
    s.left(40)
    for sa in range(5):
        s.forward(2)
        s.left(10)
    s.forward(29)

    # going down
    for sa in range(9):
        s.forward(3)
        s.left(10)
    s.forward(15)

    # going right
    for sa in range(9):
        s.forward(3)
        s.left(10)
    s.forward(26)

    # going down again
    for sa in range(9):
        s.forward(3)
        s.right(10)
    s.forward(16)

    # going left
    for sa in range(9):
        s.forward(3)
        s.right(10)
    s.forward(26)

    # going up
    for sa in range(9):
        s.forward(3)
        s.right(10)

    s.hideturtle()
    return


def draw_t(offset):
    # draws alphabet p
    t = turtle.Turtle()
    t.speed(5)
    t.color('pink')
    t.up()
    t.forward(offset)
    t.down()

    t.left(90)
    t.up()
    t.forward(100)
    t.down()
    t.right(90)
    t.forward(60)
    t.backward(30)
    t.right(90)
    t.forward(100)

    t.hideturtle()
    return


def draw_u(offset):
    # draws alphabet p
    u = turtle.Turtle()
    u.speed(5)
    u.color('white')
    u.up()
    u.forward(offset)

    u.right(90)
    u.backward(100)

    u.down()

    # start
    u.forward(75)

    # going right
    for ua in range(9):
        u.forward(4)
        u.left(10)
    u.forward(14)

    # going up
    for ua in range(9):
        u.forward(4)
        u.left(10)
    u.forward(80)

    u.hideturtle()
    return


def draw_v(offset):
    # draws alphabet v
    v = turtle.Turtle()
    v.speed(5)
    v.color('cyan')
    v.up()
    v.forward(offset)
    v.down()

    v.left(90)
    v.up()
    v.forward(100)
    v.down()
    v.right(162)
    v.forward(105)
    v.left(146)
    v.forward(104)

    v.hideturtle()
    return


def draw_w(offset):
    # draws alphabet w
    w = turtle.Turtle()
    w.speed(8)
    w.color('yellow')
    w.up()
    w.forward(offset)
    w.right(90)
    w.backward(100)
    w.down()

    # start
    w.left(14)
    w.forward(103)
    # going up
    w.left(152)
    w.forward(103)
    # turning back down
    w.right(152)
    w.forward(103)
    # going up again
    w.left(152)
    w.forward(104)

    w.hideturtle()
    return


def draw_x(offset):
    # draws alphabet x
    x = turtle.Turtle()
    x.speed(5)
    x.color('orange')
    x.up()
    x.forward(offset)
    x.down()

    x.left(59)
    x.forward(116.5)
    x.left(121)
    x.up()
    x.forward(58)
    x.down()
    x.left(121)
    x.forward(116.5)

    x.hideturtle()
    return


def draw_y(offset):
    # draws alphabet y
    y = turtle.Turtle()
    y.speed(5)
    y.color('lime')
    y.up()
    y.forward(offset)
    y.down()

    y.left(90)
    y.up()
    y.forward(99)
    y.right(90)
    y.forward(1)
    y.down()
    y.right(60)
    y.forward(58)
    y.left(120)
    y.forward(58)
    y.backward(58)
    y.right(150)
    y.forward(50)

    y.hideturtle()
    return


def draw_z(offset):
    # drawing alphabet z
    z = turtle.Turtle()
    z.speed(8)
    z.color("yellow")
    z.up()
    z.forward(offset)
    z.down()

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

    z.hideturtle()
