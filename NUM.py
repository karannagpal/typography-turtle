import turtle
# all numbers will be digital font


def draw_1(offset):
    # drawing number 1
    on = turtle.Turtle()
    on.speed(5)
    on.color("white")
    on.up()
    on.forward(offset)
    on.down()

    on.up()
    on.left(90)
    on.forward(100)
    on.right(90)
    on.forward(10)
    on.right(90)
    on.down()
    on.forward(100)

    on.hideturtle()
    return


def draw_2(offset):
    # drawing number 2
    tw = turtle.Turtle()
    tw.speed(5)
    tw.color("lime")
    tw.up()
    tw.forward(offset)
    tw.down()

    tw.left(90)
    tw.up()
    tw.forward(100)
    tw.down()
    tw.right(90)
    tw.forward(60)
    tw.right(90)
    tw.forward(50)
    tw.right(90)
    tw.forward(60)
    tw.left(90)
    tw.forward(50)
    tw.left(90)
    tw.forward(60)

    tw.hideturtle()
    return


def draw_3(offset):
    # drawing number 3
    th = turtle.Turtle()
    th.speed(5)
    th.color("cyan")
    th.up()
    th.forward(offset)
    th.down()

    th.left(90)
    th.up()
    th.forward(100)
    th.right(90)
    th.down()
    th.forward(60)
    th.right(90)
    th.forward(50)
    th.right(90)
    th.forward(50)
    th.backward(50)
    th.left(90)
    th.forward(50)
    th.right(90)
    th.forward(60)

    th.hideturtle()
    return


def draw_4(offset):
    # drawing number 4
    fo = turtle.Turtle()
    fo.speed(5)
    fo.color("orange")
    fo.up()
    fo.forward(offset)
    fo.down()

    fo.left(90)
    fo.up()
    fo.forward(100)
    fo.down()
    fo.backward(50)
    fo.right(90)
    fo.forward(60)
    fo.left(90)
    fo.forward(50)
    fo.backward(100)

    fo.hideturtle()
    return


def draw_5(offset):
    # drawing number 5
    fi = turtle.Turtle()
    fi.speed(5)
    fi.color("yellow")
    fi.up()
    fi.forward(offset)
    fi.down()

    fi.left(90)
    fi.up()
    fi.forward(100)
    fi.right(90)
    fi.forward(60)
    fi.down()
    fi.backward(60)
    fi.right(90)
    fi.forward(50)
    fi.left(90)
    fi.forward(60)
    fi.right(90)
    fi.forward(50)
    fi.right(90)
    fi.forward(60)

    fi.hideturtle()
    return


def draw_6(offset):
    # drawing number 6
    si = turtle.Turtle()
    si.speed(5)
    si.color("white")
    si.up()
    si.forward(offset)
    si.down()

    si.left(90)
    si.up()
    si.forward(100)
    si.right(90)
    si.forward(60)
    si.down()
    si.right(180)
    # start
    si.forward(60)
    si.left(90)
    si.forward(100)
    si.left(90)
    si.forward(60)
    si.left(90)
    si.forward(50)
    si.left(90)
    si.forward(60)

    si.hideturtle()
    return


def draw_7(offset):
    # drawing number 7
    se = turtle.Turtle()
    se.speed(5)
    se.color("lime")
    se.up()
    se.forward(offset)
    se.down()

    se.left(90)
    se.up()
    se.forward(100)
    se.right(90)
    se.down()
    se.forward(60)
    se.right(90)
    se.forward(100)

    se.hideturtle()
    return


def draw_8(offset):
    # drawing number 8
    ei = turtle.Turtle()
    ei.speed(5)
    ei.color("cyan")
    ei.up()
    ei.forward(offset)
    ei.down()

    ei.left(90)
    ei.forward(100)
    ei.right(90)
    ei.forward(60)
    ei.right(90)
    ei.forward(100)
    ei.right(90)
    ei.forward(60)
    ei.right(90)
    ei.forward(50)
    ei.right(90)
    ei.forward(60)

    ei.hideturtle()
    return


def draw_9(offset):
    # drawing number 9
    ni = turtle.Turtle()
    ni.speed(5)
    ni.color("pink")
    ni.up()
    ni.forward(offset)
    ni.down()

    ni.left(90)
    ni.up()
    ni.forward(50)
    ni.right(90)
    ni.forward(60)
    ni.down()
    ni.backward(60)
    ni.left(90)
    ni.forward(50)
    ni.right(90)
    ni.forward(60)
    ni.right(90)
    ni.forward(100)
    ni.right(90)
    ni.forward(60)

    ni.hideturtle()
    return


def draw_0(offset):
    # drawing number 0
    ze = turtle.Turtle()
    ze.speed(5)
    ze.color("orange")
    ze.up()
    ze.forward(offset)
    ze.down()

    ze.left(90)
    ze.forward(100)
    ze.right(90)
    ze.forward(60)
    ze.right(90)
    ze.forward(100)
    ze.right(90)
    ze.forward(60)

    ze.hideturtle()
    return
