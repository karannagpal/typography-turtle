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
    o.color("red")

    o.up()
    o.forward(offset)
    o.down()

    # check
    for oa in range(2):
        o.forward(60)
        o.left(90)
        o.forward(100)
        o.left(90)

    o.color("cyan")

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
    r.color('blue')

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
    s.color('red')

    s.up()
    s.forward(offset)
    s.down()

    # check
    for sa in range(2):
        s.forward(60)
        s.left(90)
        s.forward(100)
        s.left(90)
    s.color('white')

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
    t.color('green')

    t.up()
    t.forward(offset)
    t.down()

    # check
    for ta in range(2):
        t.forward(60)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.color('pink')

    t.hideturtle()
    return


def draw_u(offset):
    # draws alphabet p
    u = turtle.Turtle()
    u.speed(5)
    u.color('green')

    u.up()
    u.forward(offset)
    u.down()

    # check
    for ua in range(2):
        u.forward(60)
        u.left(90)
        u.forward(100)
        u.left(90)
    u.color('yellow')

    u.up()
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
    # draws alphabet p
    v = turtle.Turtle()
    v.speed(5)
    v.color('blue')

    v.up()
    v.forward(offset)
    v.down()

    # check
    for va in range(2):
        v.forward(60)
        v.left(90)
        v.forward(100)
        v.left(90)
    v.color('pink')

    v.hideturtle()
    return


def draw_w(offset):
    # draws alphabet p
    w = turtle.Turtle()
    w.speed(5)
    w.color('red')

    w.up()
    w.forward(offset)
    w.down()

    # check
    for wa in range(2):
        w.forward(100)
        w.left(90)
        w.forward(100)
        w.left(90)
    w.color('yellow')

    w.hideturtle()
    return


def draw_x(offset):
    # draws alphabet p
    x = turtle.Turtle()
    x.speed(5)
    x.color('blue')

    x.up()
    x.forward(offset)
    x.down()

    # check
    for xa in range(2):
        x.forward(60)
        x.left(90)
        x.forward(100)
        x.left(90)
    x.color('pink')

    x.hideturtle()
    return


def draw_y(offset):
    # draws alphabet p
    y = turtle.Turtle()
    y.speed(5)
    y.color('blue')

    y.up()
    y.forward(offset)
    y.down()

    # check
    for ya in range(2):
        y.forward(60)
        y.left(90)
        y.forward(100)
        y.left(90)
    y.color('pink')

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
