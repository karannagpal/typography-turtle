import turtle


def draw_n(offset):
    # drawing alphabet n
    n = turtle.Turtle()
    n.speed(8)
    n.color("cyan")

    n.up()
    n.forward(offset)
    n.down()

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


def draw_o(offset):
    # drawing alphabet o
    o = turtle.Turtle()
    o.speed(8)
    o.color("cyan")

    o.up()
    o.forward(offset)
    o.down()

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

    o.hideturtle()


def draw_p(offset):
    # draws alphabet p
    p = turtle.Turtle()
    p.speed(5)
    p.color('blue')

    p.up()
    p.forward(offset)
    p.down()

    # check
    for pa in range(2):
        p.forward(60)
        p.left(90)
        p.forward(100)
        p.left(90)
    p.color('white')

    p.left(90)
    p.forward(100)
    p.right(90)
    p.forward(10)

    for pa in range(18):
        p.forward(4.4)
        p.right(10)
    p.forward(13)

    p.hideturtle()
    return


def draw_q(offset):
    # draws alphabet q
    q = turtle.Turtle()
    q.speed(5)
    q.color('blue')

    q.up()
    q.forward(offset)
    q.down()

    # check
    for aa in range(2):
        q.forward(60)
        q.left(90)
        q.forward(100)
        q.left(90)
    q.color('yellow')

    q.left(90)
    q.up()
    q.forward(50)
    q.down()
    q.forward(20)
    for oa in range(18):
        q.right(10)
        q.forward(5.3)
    q.forward(40)
    for oa in range(18):
        q.right(10)
        q.forward(5.3)
    q.forward(20)

    q.up()
    q.right(180)
    q.forward(30)
    q.left(90)
    q.forward(30)
    q.down()
    q.right(45)
    q.forward(42.5)

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

    # check
    for pa in range(2):
        r.forward(60)
        r.left(90)
        r.forward(100)
        r.left(90)
    r.color('white')

    r.left(90)
    r.forward(100)
    r.right(90)

    r.forward(10)
    for pa in range(18):
        r.forward(4.4)
        r.right(10)

    r.forward(13)
    r.left(135)
    r.forward(75)

    r.hideturtle()
    return


def draw_s(offset):
    # draws alphabet s
    s = turtle.Turtle()
    s.speed(5)
    s.color('orange')

    s.up()
    s.forward(offset)
    s.down()

    s.hideturtle()
    return


def draw_t(offset):
    # draws alphabet p
    t = turtle.Turtle()
    t.speed(5)
    t.color('orange')

    t.up()
    t.forward(offset)
    t.down()

    t.hideturtle()
    return


def draw_u(offset):
    # draws alphabet p
    u = turtle.Turtle()
    u.speed(5)
    u.color('orange')

    u.up()
    u.forward(offset)
    u.down()

    u.hideturtle()
    return


def draw_v(offset):
    # draws alphabet p
    v = turtle.Turtle()
    v.speed(5)
    v.color('orange')

    v.up()
    v.forward(offset)
    v.down()

    v.hideturtle()
    return


def draw_w(offset):
    # draws alphabet p
    w = turtle.Turtle()
    w.speed(5)
    w.color('orange')

    w.up()
    w.forward(offset)
    w.down()

    w.hideturtle()
    return


def draw_x(offset):
    # draws alphabet p
    x = turtle.Turtle()
    x.speed(5)
    x.color('orange')

    x.up()
    x.forward(offset)
    x.down()

    x.hideturtle()
    return


def draw_y(offset):
    # draws alphabet p
    y = turtle.Turtle()
    y.speed(5)
    y.color('orange')

    y.up()
    y.forward(offset)
    y.down()

    y.hideturtle()
    return


def draw_z(offset):
    # drawing alphabet z
    z = turtle.Turtle()
    z.speed(8)
    z.color("orange")

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

    # check
    '''
    z.left(90)
    z.forward(100)
    '''
    z.hideturtle()
