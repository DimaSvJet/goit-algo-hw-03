import turtle


def draw_pythagoras_tree(t, length, depth):
    if depth == 0:
        t.forward(length)
        t.backward(length)
    else:
        t.forward(length)
        t.left(45)
        draw_pythagoras_tree(t, length * 0.707, depth-1)
        t.right(90)
        draw_pythagoras_tree(t, length * 0.707, depth-1)
        t.left(45)
        t.backward(length)


def main(depth):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.color("green")
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.speed(0)

    draw_pythagoras_tree(t, 200, depth)

    window.mainloop()


if __name__ == "__main__":
    a = int(input('Enter level: '))
    main(a)
