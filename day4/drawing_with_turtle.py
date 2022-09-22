import sys
import turtle


def draw_rectangle():
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)


def draw_circle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()

def draw_triangle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(80, 98)
    pen.down()
    pen.begin_fill()
    pen.pencolor("green")
    pen.fillcolor("yellow")
    pen.forward(100)  # draw base

    pen.left(120)
    pen.forward(100)

    pen.left(120)
    pen.forward(100)
    pen.end_fill()
    pen.up()

def draw_pentagon():


    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(-130, -158)
    pen.down()
    pen.begin_fill()
    pen.pencolor("green")
    pen.fillcolor("brown")
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.end_fill()
    pen.up()

def text_amaizing():
    turtle.color('black')
    style('Arial',30,'italic')
    turtle.write('Hello princess',font=style,align='center')
    turtle.hideturtle()

def main():
    draw_rectangle()
    draw_circle()
    draw_triangle()
    draw_pentagon()
    text_amaizing()
    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
