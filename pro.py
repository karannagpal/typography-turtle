import turtle
import A2M
import N2Z
import SP
import NUM


def display(name):
    window = turtle.Screen()
    window.screensize(1300, 500)
    window.bgcolor("#222")

    offset = 0 - (len(name) * 40)

    name = name.lower()

    # offset variable in each function's argument
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
            A2M.draw_d(offset)
            offset = offset + 80
        if i == 'e':
            A2M.draw_e(offset)
            offset = offset + 80
        if i == 'f':
            A2M.draw_f(offset)
            offset = offset + 80
        if i == 'g':
            A2M.draw_g(offset)
            offset = offset + 80
        if i == 'h':
            A2M.draw_h(offset)
            offset = offset + 80
        if i == 'i':
            A2M.draw_i(offset)
            offset = offset + 40
        if i == 'j':
            A2M.draw_j(offset)
            offset = offset + 80
        if i == 'k':
            A2M.draw_k(offset)
            offset = offset + 80
        if i == 'l':
            A2M.draw_l(offset)
            offset = offset + 80
        if i == 'm':
            A2M.draw_m(offset)
            offset = offset + 100

        if i == 'n':
            N2Z.draw_n(offset)
            offset = offset + 80
        if i == 'o':
            N2Z.draw_o(offset)
            offset = offset + 80
        if i == 'p':
            N2Z.draw_p(offset)
            offset = offset + 80
        if i == 'q':
            N2Z.draw_q(offset)
            offset = offset + 80
        if i == 'r':
            N2Z.draw_r(offset)
            offset = offset + 80
        if i == 's':
            N2Z.draw_s(offset)
            offset = offset + 80
        if i == 't':
            N2Z.draw_t(offset)
            offset = offset + 80
        if i == 'u':
            N2Z.draw_u(offset)
            offset = offset + 80
        if i == 'v':
            N2Z.draw_v(offset)
            offset = offset + 80
        if i == 'w':
            N2Z.draw_w(offset)
            offset = offset + 120
        if i == 'x':
            N2Z.draw_x(offset)
            offset = offset + 80
        if i == 'y':
            N2Z.draw_y(offset)
            offset = offset + 80
        if i == 'z':
            N2Z.draw_z(offset)
            offset = offset + 80

        if i == ' ':
            SP.draw_space(offset)
            offset = offset + 60
        if i == '.':
            SP.draw_dot(offset)
            offset = offset + 20
        if i == '-':
            SP.draw_dash(offset)
            offset = offset + 80

        if i == '1':
            NUM.draw_1(offset)
            offset = offset + 40
        if i == '2':
            NUM.draw_2(offset)
            offset = offset + 80
        if i == '3':
            NUM.draw_3(offset)
            offset = offset + 80
        if i == '4':
            NUM.draw_4(offset)
            offset = offset + 80
        if i == '5':
            NUM.draw_5(offset)
            offset = offset + 80
        if i == '6':
            NUM.draw_6(offset)
            offset = offset + 80
        if i == '7':
            NUM.draw_7(offset)
            offset = offset + 80
        if i == '8':
            NUM.draw_8(offset)
            offset = offset + 80
        if i == '9':
            NUM.draw_9(offset)
            offset = offset + 80
        if i == '0':
            NUM.draw_0(offset)
            offset = offset + 80

    window.exitonclick()

    return
