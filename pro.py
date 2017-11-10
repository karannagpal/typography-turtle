import turtle
import A2M
import N2Z
import SP


def display(name):
    window = turtle.Screen()
    window.bgcolor("#222")

    offset = 0 - (len(name)/2)

    name = name.lower()

    # place offset variable in each function's argument
    for i in name:
        if i == 'a':
            A2M.draw_a(offset)
            offset = offset + 80
        if i == 'b':
            A2M.draw_b(offset)
            offset = offset + 80
        if i == 'c':
            A2M.draw_c(offset)
            offset = offset + 80
        if i == 'd':
            A2M.draw_d()
        if i == 'e':
            A2M.draw_e()
        if i == 'f':
            A2M.draw_f()
        if i == 'g':
            A2M.draw_g()
        if i == 'h':
            A2M.draw_h()
        if i == 'i':
            A2M.draw_i()
        if i == 'j':
            A2M.draw_j()
        if i == 'k':
            A2M.draw_k()
        if i == 'l':
            A2M.draw_l()
        if i == 'm':
            A2M.draw_m()

        if i == 'n':
            N2Z.draw_n()
        if i == 'o':
            N2Z.draw_o()
        if i == 'p':
            N2Z.draw_p()
        if i == 'q':
            N2Z.draw_q()
        if i == 'r':
            N2Z.draw_r()
        if i == 's':
            N2Z.draw_s()
        if i == 't':
            N2Z.draw_t()
        if i == 'u':
            N2Z.draw_u()
        if i == 'v':
            N2Z.draw_v()
        if i == 'w':
            N2Z.draw_w()
        if i == 'x':
            N2Z.draw_x()
        if i == 'y':
            N2Z.draw_y()
        if i == 'z':
            N2Z.draw_z()

        if i == ' ':
            SP.draw_space()
        if i == '.':
            SP.draw_dot()
        if i == '-':
            SP.draw_dash()

    window.exitonclick()


