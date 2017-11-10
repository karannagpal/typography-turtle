'''
import turtle
import A2M
import N2Z
import SP
'''


def k():
    print("This is k")
    return


def a():
    print("This is a")
    return


def r():
    print("This is r")
    return


def n():
    print("This is n")
    return


def e():
    print("This is e")
    return


def t():
    print("This is t")
    return


def b():
    print("This is b")
    return


def s():
    print("This is s")
    return


def l():
    print("This is l")
    return


def h():
    print("This is h")
    return


def space():
    print("Space here")
    return

name = str(input("Enter your name: "))
dist = 0

name = name.lower()

for i in name:
    if i == 'a':
        print(" " * dist, end="")
        a()
    if i == 'b':
        print(" " * dist, end="")
        b()
    if i == 'c':
        print(" " * dist, end="")
        c()
    if i == 'd':
        print(" " * dist, end="")
        d()
    if i == 'e':
        print(" " * dist, end="")
        e()
    if i == 'f':
        print(" " * dist, end="")
        f()
    if i == 'g':
        print(" " * dist, end="")
        g()
    if i == 'h':
        print(" " * dist, end="")
        h()
    if i == 'i':
        print(" " * dist, end="")
        pri()
    if i == 'j':
        print(" " * dist, end="")
        j()
    if i == 'k':
        print(" " * dist, end="")
        k()
    if i == 'l':
        print(" " * dist, end="")
        l()
    if i == 'm':
        print(" " * dist, end="")
        m()

    if i == 'n':
        print(" " * dist, end="")
        n()
    if i == 'o':
        print(" " * dist, end="")
        p()
    if i == 'p':
        print(" " * dist, end="")
        n()
    if i == 'q':
        print(" " * dist, end="")
        q()
    if i == 'r':
        print(" " * dist, end="")
        r()
    if i == 's':
        print(" " * dist, end="")
        s()
    if i == 't':
        print(" " * dist, end="")
        t()
    if i == 'u':
        print(" " * dist, end="")
        u()
    if i == 'v':
        print(" " * dist, end="")
        v()
    if i == 'w':
        print(" " * dist, end="")
        w()
    if i == 'x':
        print(" " * dist, end="")
        x()
    if i == 'y':
        print(" " * dist, end="")
        y()
    if i == 'z':
        print(" " * dist, end="")
        z()

    if i == ' ':
        print(" " * dist, end="")
        space()
    if i == '.':
        print(" " * dist, end="")
        dot()
    if i == ',':
        print(" " * dist, end="")
        comma()

    dist = dist + 2